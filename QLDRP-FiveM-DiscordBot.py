# Made by epell1 for QLDRP FiveM (discord.gg/qldrp)

#                 _                                       _ _       _                _                                  _   
#                | |                                     | | |     | |              | |                                | |  
#   ___ _ __   __| | _____   __  ______    ___ _ __   ___| | |   __| | _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
#  / _ \ '_ \ / _` |/ _ \ \ / / |______|  / _ \ '_ \ / _ \ | |  / _` |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
# |  __/ |_) | (_| |  __/\ V /           |  __/ |_) |  __/ | | | (_| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
#  \___| .__/ \__,_|\___| \_/             \___| .__/ \___|_|_|  \__,_|\___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
#      | |                                    | |                                           | |                             
#      |_|                                    |_|                                           |_|     
#
# epdev - epell development | Pushing for the future of development

# Imports
from itertools import count
import random
from tracemalloc import stop
from turtle import color, title
import discord
from discord.ext import commands
import os
import json
import asyncio
from os.path import join, dirname
# import ts3
# from dotenv import load_dotenv

# Versions
botversion = "V.0.2"
botlibrary = f"PyCord V.{discord.__version__}"

# Variables
bot = discord.Bot(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix='$')
bot.remove_command('help')
botname = "QLDRP Assistant"
boticon = "https://images-ext-2.discordapp.net/external/QVv_r9z2BrtyU5yopCaFtyvDHQ58MEgZg-G9F_TQ71E/%3Fsize%3D512/https/cdn.discordapp.com/icons/963240374791454780/974ea0bf7c95692d150d02bbac1c85ff.png?width=662&height=662"

# Intial Messages
os.system('cls')
print(f'{botname} | {botversion} | {botlibrary}')
print("---------------------------")
print("Starting Bot Tests")

# Random status messages
o = "o"
statusmessages = [
    "connect join.qldrp.com:30120",
    "QLDRP FiveM Server",
    f'{botversion} | {botlibrary}'
]
status = random.choice(statusmessages)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb)
    print('Main Bot Status: Running')
    print(f'Bot Connection: Ok')
    print("Startup Latency: {0}ms".format(round(bot.latency, 1)))
    print(f'Current Bot Version: {botversion}')
    print(f'Current Bot Library: {botlibrary}')
    print("---------------------------")
    print("Error Logs:")
    while o == "o":
        await asyncio.sleep(5)
        status = random.choice(statusmessages)
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=status))
    await asyncio.sleep(21600)
    os.system('py qldrpfivem-bot.py')
    exit()

# Basic Commands
@bot.slash_command(description="Gets the latency of the discord bot!")
async def ping(ctx):
    pingembed = discord.Embed(
        colour=discord.Colour.blue(),
        title="",
        description=""
    )
    pingembed.set_author(name=botname, icon_url=boticon)
    pingembed.add_field(name="Ping", value="Pong! The bots ping is currently ``{0}ms``".format(round(bot.latency, 1)), inline=True)
    pingembed.set_footer(text="Made with ❤ by epell development | {0}ms".format(round(bot.latency, 1)))
    await ctx.respond(embed=pingembed, ephemeral=True)
    print("Ping Command: Latency: {0}ms".format(round(bot.latency, 1)))

@bot.slash_command(description="Shows information of the bot!")
async def info(ctx):
    infoembed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Information",
        description=""
    )
    infoembed.set_author(name=botname, icon_url=boticon)
    infoembed.add_field(name="Purpose", value="This bot made by epell1 for the QLDRP FiveM discord server", inline=True)
    infoembed.add_field(name="Bot Info", value=f"Library: ``{botlibrary}``\nBot Version: ``{botversion}``\nLatency: ``{0}ms``".format(round(bot.latency, 1)), inline=True)
    infoembed.set_footer(text="Made with ❤ by epell development | {0}ms".format(round(bot.latency, 1)))
    await ctx.respond(embed=infoembed, ephemeral=True)
    
@bot.slash_command(description="Get an invite to the QLDRP FiveM discord server!")
async def invite(ctx):
    await ctx.respond(f'https://discord.gg/hhqQ6h2kKG', ephemeral=True)

@bot.slash_command(description="Get connection details to the FiveM server!")
async def fivemserver(ctx):
    await ctx.respond(f'``connect join.qldrp.com:30120``', ephemeral=True)

@bot.slash_command(description="Get a link to the CAD/MDT system")
async def cad(ctx):
    await ctx.respond(f'https://cad.qldrp.com', ephemeral=True)

@bot.slash_command(description="Get a list of approved flight schools in QLDRP!!")
async def flightschools(ctx):
    flightschoolsembed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Approved Flight Schools",
        description="These flight schools are the ONLY approved ones for use in QLDRP | FiveM."
    )
    flightschoolsembed.add_field(name="EFS - epell's flight school", value="https://epdev.adalo.com/efs-v2/", inline=True)
    flightschoolsembed.add_field(name="SFS - Saddle's flight school", value="DM <@1136530284339265596>", inline=True)
    await ctx.respond(embed=flightschoolsembed, ephemeral=True)

# Reaction Roles
OUTAGE_ROLE_ID = 989761609121554512
UPDATES_ROLE_ID = 989768417965907988
message_id = None

@bot.slash_command(description="Set up reaction roles.")
async def setup_reaction_roles(ctx):
    role_id = 1026902857829589102
    roleid = discord.utils.get(ctx.author.roles, id=role_id)
    if roleid is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    global message_id
    rrembed = discord.Embed(
        colour=discord.Colour.blue(),
        title="Reaction Roles",
        description="Get certain roles by reacting to this message! These can be mentions or other roles!"
    )
    rrembed.add_field(name="Outage Alerts", value="React with <:Q5PDOutage:1005491584353185832> to be notified when the server is down, out, or being restarted!", inline=True)
    rrembed.add_field(name="Updates", value="React with <:update:989767017366175755> to be notified of an update to the server!", inline=True)
    message = await ctx.send(embed=rrembed)
    message_id = message.id
    emojis = ["<:Q5PDOutage:1005491584353185832>", "<:update:989767017366175755>"]
    for emoji in emojis:
        await message.add_reaction(emoji)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == message_id:
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if str(payload.emoji) == '<:Q5PDOutage:1005491584353185832>':
            role = discord.utils.get(guild.roles, id=OUTAGE_ROLE_ID)
            await member.add_roles(role)
        elif str(payload.emoji) == '<:update:989767017366175755>':
            role = discord.utils.get(guild.roles, id=UPDATES_ROLE_ID)
            await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == message_id:
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if member is not None:
            if str(payload.emoji) == '<:Q5PDOutage:1005491584353185832>':
                role = discord.utils.get(guild.roles, id=OUTAGE_ROLE_ID)
                if role is not None:
                    await member.remove_roles(role)
                else:
                    print(f"Role with ID {OUTAGE_ROLE_ID} not found.")
            elif str(payload.emoji) == '<:update:989767017366175755>':
                role = discord.utils.get(guild.roles, id=UPDATES_ROLE_ID)
                if role is not None:
                    await member.remove_roles(role)
                else:
                    print(f"Role with ID {UPDATES_ROLE_ID} not found.")
        else:
            print(f"Member with ID {payload.user_id} not found.")

# Administration Commands

def has_role(role_id):
    async def predicate(ctx):
        role = discord.utils.get(ctx.author.roles, id=role_id)
        return role is not None

    return commands.check(predicate)

@bot.slash_command(name='purge', description="Remove messages from a channel! (Default is 10)")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.respond(f'Purged {amount} of messages!', ephemeral=True)

@bot.slash_command(name="say", description="Has the bot repeat a message back to you!")
@commands.has_permissions(manage_messages=True)
async def repeat(ctx, *, message):
    await ctx.respond(f'Sending message `{message}` to chat', ephemeral=True)
    await ctx.send(message)

@bot.slash_command(name="sayembed", description="Has the bot repeat a message back to you as an embed!")
@commands.has_permissions(manage_messages=True)
async def sayembed(ctx, *, message):
    socialsembed = discord.Embed(
        colour=discord.Colour.blue(),
        title="",
        description=""
    )
    socialsembed.set_author(name=botname, icon_url=boticon)
    socialsembed.add_field(name=" ", value=message)
    socialsembed.set_footer(text=f"Made with ❤ by epell development")

    await ctx.respond(f'Sending message `{message}` to chat as an embed', ephemeral=True)
    await ctx.respond(embed=socialsembed)

@bot.slash_command(name="assignrole", description="Assign a role to a user.")
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    role_id = 963351345245589514
    permisson = discord.utils.get(ctx.author.roles, id=role_id)
    if permisson is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    if role in member.roles:
        try:
            await member.remove_roles(role)
            await ctx.respond(f"✅ | Successfully removed {role.name} from {member.mention}", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond("❌ | I don't have the necessary permissions to remove roles.", ephemeral=True)
        except discord.HTTPException:
            await ctx.respond("❌ | An error occurred while removing the role.", ephemeral=True)
    else:
        try:
            await member.add_roles(role)
            await ctx.respond(f"✅ | Successfully assigned {role.name} to {member.mention}", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond("❌ | I don't have the necessary permissions to assign roles.", ephemeral=True)
        except discord.HTTPException:
            await ctx.respond("❌ | An error occurred while assigning the role.", ephemeral=True)

# Blacklist Commands
blacklist = bot.create_group("blacklist", "Manage a user's whitelist application results")

def save_blacklist_to_file(user_id, blacklist_id, blacklist_type, reason):
    with open("blacklist.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - ID: {blacklist_id}, User ID: {user_id}, Type: {blacklist_type}, Reason: {reason}\n")

class RevokeButton(discord.ui.Button):
    def __init__(self, user_id, blacklist_id):
        super().__init__(style=discord.ButtonStyle.red, label="Revoke Blacklist")
        self.user_id = user_id
        self.blacklist_id = blacklist_id

    async def callback(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("Blacklist revoked!", ephemeral=True)
        except CommandError as e:
            await interaction.response.send_message(f"Error: {e}", ephemeral=True)

@blacklist.command(description="Blacklist a user from QLDRP FiveM")
async def user(ctx, *, user: discord.User, blacklist_type, reason, justification, approved_by: discord.User):
    role_id1 = 963350668846981120
    role_id2 = 1155370698240430110
    role1 = discord.utils.get(ctx.author.roles, id=role_id1)
    role2 = discord.utils.get(ctx.author.roles, id=role_id2)
    if role1 is None and role2 is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    response_channel_id = 963345333574828043
    response_channel = ctx.bot.get_channel(response_channel_id)
    blacklist_type = blacklist_type.lower()
    if blacklist_type == "a":
        blacklist_type = "A (Permanent, Unappealable)"
    elif blacklist_type == "b":
        blacklist_type = "B (Permanent, Appealable)"
    elif blacklist_type == 'c':
        blacklist_type = 'C (3 to 5 Years, Appealable)'
    elif blacklist_type == 'd':
        blacklist_type = 'D (2 to 1 Year/s, Appealable)'
    elif blacklist_type == 'e':
        blacklist_type = 'E (1 Year to 6 months, Appealable)'
    elif blacklist_type == 'f':
        blacklist_type = 'F (5 to 2 Months, Appealable)'
    elif blacklist_type == 'g':
        blacklist_type = 'G (< 1 Month, Appealable)'
    else:
        await ctx.respond(f"❌ | Not a valid type, Must be from A-G.", ephemeral=True)
        return
    
    blacklistembed = discord.Embed(
        colour=discord.Colour.red(),
        title="",
        description=""
    )
    blacklistembed.add_field(name="User Blacklist", value=f"User: {user.mention}\nType: {blacklist_type}\nReason: {reason}\nJustification: {justification}\nApproved By: {approved_by.mention}")
    if user is not None:
        try:
            await user.send(embed=blacklistembed)
            await ctx.respond(f"✅ | Successfully Blacklisted {user.mention}", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond("❌ | I don't have permission to send a DM to this user.", ephemeral=True)
    else:
        await ctx.respond("❌ | User not found.")
    await ctx.guild.ban(user, reason=f'{blacklist_type} | {reason}')
    await response_channel.send(embed=blacklistembed)

@blacklist.command(description="Blacklist a server from QLDRP FiveM")
async def server(ctx, *, server, invite, blacklist_type, reason, justification, approved_by: discord.User):
    role_id1 = 1144172526281441340
    role_id2 = 1155370698240430110
    role1 = discord.utils.get(ctx.author.roles, id=role_id1)
    role2 = discord.utils.get(ctx.author.roles, id=role_id2)
    if role1 is None and role2 is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    response_channel_id = 963345333574828043
    response_channel = ctx.bot.get_channel(response_channel_id)
    approved_by = approved_by.mention
    blacklist_type = blacklist_type.lower()
    if blacklist_type == "a":
        blacklist_type = "A (Permeant, Unappealable)"
    elif blacklist_type == "b":
        blacklist_type = "B (Permeant, Appealable)"
    elif blacklist_type == 'c':
        blacklist_type = 'C (3 to 5 Years, Appealable)'
    elif blacklist_type == 'd':
        blacklist_type = 'D (2 to 1 Year/s, Appealable)'
    elif blacklist_type == 'e':
        blacklist_type = 'E (1 Year to 6 months, Appealable)'
    elif blacklist_type == 'f':
        blacklist_type == 'F (5 to 2 Months, Appealable)'
    elif blacklist_type == 'g':
        blacklist_type == 'G (< 1 Month, Appealable)'
    else:
        await ctx.respond(f"❌ | Not a valid type, Must be from A-G.", ephemeral=True)
        return
    serverblacklistembed = discord.Embed(
        colour=discord.Colour.red(),
        title="",
        description=""
    )
    serverblacklistembed.add_field(name="Server Blacklist", value=f"Server: {server} ({invite})\nType: {blacklist_type}\nReason: {reason}\nJustification: {justification}\nApproved By: {approved_by}")
    await ctx.respond(f"✅ | Successfully Blacklisted {server}", ephemeral=True)
    await response_channel.send(embed=serverblacklistembed)

@blacklist.command(description="Unblacklist a user")
async def user_revoke(ctx, *, user: discord.User, blacklist_type, reason, approved_by: discord.User):
    role_id1 = 1144172526281441340
    role_id2 = 1155370698240430110
    role1 = discord.utils.get(ctx.author.roles, id=role_id1)
    role2 = discord.utils.get(ctx.author.roles, id=role_id2)
    if role1 is None and role2 is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    response_channel_id = 1072412277912899594
    response_channel = ctx.bot.get_channel(response_channel_id)
    blacklist_type = blacklist_type.lower()
    if blacklist_type == "a":
        blacklist_type = "A (Permanent, Unappealable)"
    elif blacklist_type == "b":
        blacklist_type = "B (Permanent, Appealable)"
    elif blacklist_type == 'c':
        blacklist_type = 'C (3 to 5 Years, Appealable)'
    elif blacklist_type == 'd':
        blacklist_type = 'D (2 to 1 Year/s, Appealable)'
    elif blacklist_type == 'e':
        blacklist_type = 'E (1 Year to 6 months, Appealable)'
    elif blacklist_type == 'f':
        blacklist_type = 'F (5 to 2 Months, Appealable)'
    elif blacklist_type == 'g':
        blacklist_type = 'G (< 1 Month, Appealable)'
    else:
        await ctx.respond(f"❌ | Not a valid type, Must be from A-G.", ephemeral=True)
        return
    unblacklistembed = discord.Embed(
        colour=discord.Colour.red(),
        title="",
        description=""
    )
    unblacklistembed.add_field(name="Blacklist Revoked", value=f"User: {user.mention}\nBlacklist Type: {blacklist_type}\nReason for revoke: {reason}\nApproved By: {approved_by.mention}")
    await ctx.respond(f"✅ | Successfully Revoked the Blacklist for: {user.mention}", ephemeral=True)
    await ctx.guild.unban(user)
    await response_channel.send(embed=unblacklistembed)

@blacklist.command(description="Search for a blacklist by ID")
async def search(ctx, blacklist_id: str):
    with open("blacklist.txt", "r") as file:
        blacklist_data = file.readlines()

    for entry in blacklist_data:
        if f"ID: {blacklist_id}," in entry:
            parts = entry.split(" - ")
            timestamp = parts[0]
            info = parts[1]
            blacklist_embed = discord.Embed(
                title=f"Blacklist ID: {blacklist_id}",
                description=f"Timestamp: {timestamp}\n{info}",
                color=discord.Color.red()
            )
            row = discord.ui.ActionRow(RevokeButton(ctx.author.id, blacklist_id))
            await ctx.send(embed=blacklist_embed, components=[row])
            return
    await ctx.send(f"No blacklist found with ID: {blacklist_id}")


# Whitelist Commands
application = bot.create_group("application", "Manage a users whitelist application results")

@application.command(name="pass", description="Assign a specific role to a user and send a DM.")
async def accept(ctx, user: discord.User, notes: str = None):
    role_id = 1153610596458188840
    role = ctx.guild.get_role(role_id)
    if role is None:
        await ctx.respond("❌ The specified role was not found.", ephemeral=True)
        return
    role_id_check = 1144172526281441340
    role_check = discord.utils.get(ctx.author.roles, id=role_id_check)
    response_channel_id = 1153656182662254662
    response_channel = ctx.bot.get_channel(response_channel_id)

    if role_check is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return

    user_id = user.id
    member = ctx.guild.get_member(user_id)
    role = ctx.guild.get_role(role_id)
    if role is None:
        await ctx.respond("❌ The role could not be found.", ephemeral=True)
        return
    if member is None:
        await ctx.respond("❌ User not found in this server.", ephemeral=True)
        return
    try:
        await member.add_roles(role, reason="Role assigned by command")
        await ctx.respond(f"✅ | Whitelisted {user.mention}!", ephemeral=True)
    except discord.Forbidden:
        await ctx.respond("❌ I couldn't assign the role to this user. Please check my permissions or if the user already has the role.", ephemeral=True)
    try:
        dm_message = "You have **PASSED** your whitelisted civilian application in QLDRP FiveM. Congratulations!"
        await user.send(dm_message)
    except discord.Forbidden:
        await ctx.respond("❌ I couldn't send a DM to the user.", ephemeral=True)

    whitelistembed = discord.Embed(
        title="Application Result",
        description=f"User: {user.mention}\nResult: **PASS**\nNotes: {notes}",
        color=discord.Colour.green()
    )
    await response_channel.send(embed=whitelistembed)

@application.command(description="Assign a specific role to a user and send a DM.")
async def deny(ctx, user: discord.User, notes: str = None):
    role = 1153610596458188840
    role_id = 1144172526281441340
    roleid = discord.utils.get(ctx.author.roles, id=role_id)
    response_channel_id = 1153656182662254662
    response_channel = ctx.bot.get_channel(response_channel_id)
    if roleid is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    member = ctx.guild.get_member(user.id)
    if member is None:
        await ctx.respond("❌ User not found in this server.", ephemeral=True)
        return
    try:
        dm_message = "You have **FAILED** your whitelisted civillian application in QLDRP FiveM."
        await user.send(dm_message)
    except discord.Forbidden:
        await ctx.respond("❌ I couldn't send a DM to the user.", ephemeral=True)
    failembed = discord.Embed(
        title="",
        description=f"",
        color=discord.Colour.red()
    )
    failembed.add_field(name="Application Result", value=f"User: {user.mention}\nResult: **FAIL**\nNotes: {notes}")
    await response_channel.send(embed=failembed)
    await ctx.respond(f"✅ | Denied {user.mention}'s application!", ephemeral=True)

# SSU Commands
server = bot.create_group("server", "Commands to manage server sessions")

@server.command(description="Starts the server!")
async def up(ctx, imageurl):
    role_id = 1144172526281441340
    role = discord.utils.get(ctx.author.roles, id=role_id)

    if role is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return

    if not imageurl.lower().endswith(('.jpg', '.png')):
        await ctx.respond("❌ Invalid image URL. Only .jpg and .png URLs are allowed.", ephemeral=True)
        return
    
    response_channel_id = 1027766607222669322
    response_channel = ctx.bot.get_channel(response_channel_id)
    ssuembed = discord.Embed(
        colour=discord.Colour.green(),
        title="",
        description=""
    )
    ssuembed.add_field(name="✅ | Server up!", value=f"An SSU has been activated by {ctx.author.mention}.\nIf you voted please join [here](https://cfx.re/join/y6vrly)")
    ssuembed.set_image(url=imageurl)
    ssuembed.set_footer(text="Even though SSU's are hosted, You may join the server at any time!")
    async for message in response_channel.history(limit=2):
        if not message.pinned:
            await message.delete()
    await response_channel.send(f'@here', allowed_mentions=discord.AllowedMentions(everyone=True))
    await response_channel.send(embed=ssuembed)
    await ctx.respond('✅ | Server Started!', ephemeral=True)

@server.command(description="Shuts down the server!")
async def down(ctx):
    role_id = 1144172526281441340
    role = discord.utils.get(ctx.author.roles, id=role_id)
    if role is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    response_channel_id = 1027766607222669322
    response_channel = ctx.bot.get_channel(response_channel_id)
    ssdembed = discord.Embed(
        colour=discord.Colour.red(),
        title="",
        description=""
    )
    ssdembed.add_field(name="⛔ | Server Down!", value=f"The previous SSU has been closed by {ctx.author.mention}.\nYou may still join the server at any time!")
    ssdembed.set_footer(text="Even though SSU's are hosted, You may join the server at any time!")
    async for message in response_channel.history(limit=2):
        if not message.pinned:
            await message.delete()
    await response_channel.send(embed=ssdembed)
    await ctx.respond('✅ | Server Shutdown!', ephemeral=True)

@server.command(description="Starts a vote for the server to be started!")
async def poll(ctx, *, time):
    requiredvotes = 7
    role_id = 1144172526281441340
    role = discord.utils.get(ctx.author.roles, id=role_id)
    if role is None:
        await ctx.respond("❌ You don't have permission to use this command.", ephemeral=True)
        return
    response_channel_id = 1027766607222669322
    response_channel = ctx.bot.get_channel(response_channel_id)
    ssupollembed = discord.Embed(
        colour=discord.Colour.red(),
        title="",
        description=""
    )
    ssupollembed.add_field(name="📜 | Server Poll!", value=f"{ctx.author.mention} has started a SSU Vote for {time} ± 20mins.\nWe require {requiredvotes}+ to start the server!")
    ssupollembed.set_footer(text="Even though SSU's are hosted, You may join the server at any time!")
    async for message in response_channel.history(limit=1):
        if not message.pinned:
            await message.delete()
    await response_channel.send(f'@here', allowed_mentions=discord.AllowedMentions(everyone=True))
    response_message = await response_channel.send(embed=ssupollembed)
    try:
        await response_message.add_reaction('✅')
    except Exception as e:
        await ctx.respond('❌ | Error adding reaction, Please do this manually!', ephemeral=True)
    await ctx.respond('✅ | Server Vote Started!', ephemeral=True)


# CASA Commands
casa = bot.create_group("casa", "Civil Aviation Safety Authority")

@casa.command(description="Give or remove a specific pilot's license")
async def toggle_license(ctx, *, user: discord.User, license: int):
    role_ids = {
        1: 1034773390575292469,  # Recreational Pilots License
        2: 1035479875118694441,  # Recreational Pilots License (Helicopter)
        3: 1034774687126921227   # Commercial Pilots License
    }
    role_id = role_ids.get(license)
    if role_id is None:
        await ctx.respond("❌ Invalid license selected.", ephemeral=True)
        return
    role = ctx.guild.get_role(role_id)
    if role is None:
        await ctx.respond("❌ The role associated with the selected license does not exist.", ephemeral=True)
        return
    try:
        member = ctx.guild.get_member(user.id)
        if member is None:
            await ctx.respond("❌ User not found in this server.", ephemeral=True)
            return
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.respond(f"✅ {user.mention} has been removed from the {role.name} role.", ephemeral=True)
        else:
            await member.add_roles(role)
            await ctx.respond(f"✅ {user.mention} has been assigned the {role.name} role!", ephemeral=True)
    except discord.Forbidden:
        await ctx.respond("❌ I couldn't modify the roles for this user. Ensure I have the correct permissions.", ephemeral=True)


# All Non-Bot Management Commands Above!

print("Bot Command Status: Running")

# Bot Management Commands
@bot.slash_command(description="Shut down the discord bot! (Restricted to epell1 only)")
@commands.is_owner()
async def quit(ctx):
    await ctx.respond("Shutting bot down!", ephemeral=True)
    exit()
@bot.slash_command(description="Restart the discord bot! (Restricted to epell1 only)")
@commands.is_owner()
async def restart(ctx):
    await ctx.respond("Restarting Bot", ephemeral=True)
    os.system('py qldrpfivem-bot.py')
    exit()

# Error Messages
@quit.error
async def quit_error(ctx, error):
    await ctx.respond("You do not have permission to run this command!")
    print(f'Quit Command: User tried to run the Quit Command')

@clear.error
async def purge_error(ctx, error):
    await ctx.respond("You do not have permission to run this command!", ephemeral=True)

@repeat.error
async def repeat_error(ctx, error):
    await ctx.respond("You do not have permission to run this command!", ephemeral=True)

print("Error Messages Status: Running")

bot.run('NUH UH BUD')

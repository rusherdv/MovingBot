import discord
from time import sleep


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('$>...')
        await client.change_presence(activity=discord.Streaming(name="rusher#3981", url="https://www.twitch.tv/rusherdv_"))
        channel = client.get_channel("MAIN CHANNEL ON THE SERVER")
        #await channel.send('**I'MMMM REAAAADYYYY**')
        #await channel.send('https://pa1.narvii.com/7105/e33076aa868b588d5ac7633865ff4cfd1f2199c3r1-500-271_hq.gif')
        
    async def on_message(self, message):
        
        if message.content.startswith('!how'):
        
            user = message.author
            await message.reply("How to use **!move**? easy")
            await message.channel.send('!move @name times')

        if message.content.startswith('!mover'):
        
            try:
                user = message.author
                mention = message.mentions[0]
            except IndexError:
                await message.channel.send("You haven't specified the name")
                return
                
            try:
                vueltas = message.content[29]
                lol1 = await message.channel.send('Okay')
                lol2 = await message.channel.send('Moving ' + str(mention) + "...")
                print(str(user) + "has excute !move")
                
                sleep(2)
                
                await message.delete()
                await lol1.delete()
                await lol2.delete()
                voice_channels = [channel for channel in message.guild.voice_channels]
                
                v = 0
                
                while v < int(vueltas):
                    v = v + 1
                    for channel in voice_channels:
                        await mention.move_to(channel)
            except IndexError:
                await message.channel.send("You haven't specified the times")
                          
   
            
            


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
            
client.run("BOT TOKEN")
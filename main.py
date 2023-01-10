import discum
import time 
import colorama
import os
from sty import fg

reset = colorama.Fore.RESET

os.system("cls")

text1 = f'''
     

██████╗  █████╗ ██████╗  ██████╗ ███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██║  ██║██║  ███╗█████╗      ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══██║██║  ██║██║   ██║██╔══╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██████╔╝╚██████╔╝███████╗    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝



'''

text = text1.replace('$', f'{fg(240, 179, 255)}$').replace('\\', reset+'\\').replace('|', reset+'|').replace('/', reset+'/').replace('>', reset+'>')+reset

print(text)

token = str(input(f"{fg(255,0,0)}   [1] Token da Conta >> {reset}"))
guild_id = str(input(f"{fg(255,0,0)}   [2] ID do Servidor >> {reset}"))
channel_id = str(input(f"{fg(255,0,0)}   [3] ID do Canal >> {reset}"))
print('\n\n')
bot = discum.Client(token= token, log=True)
bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' membros buscados')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()


def __get_badges(flags) -> list[str]:
    
        BADGES = {
            1 << 1:  'Partnered Server Owner',
            1 << 2:  'HypeSquad Events',
            1 << 3:  'Bug Hunter Level 1',
            1 << 9:  'Early Supporter',
            1 << 10: 'Team User',
            1 << 14: 'Bug Hunter Level 2',
            1 << 17: 'Early Verified Bot Developer',
            1 << 18: 'Discord Certified Moderator'
        }

        badges = []

        for badge_flag, badge_name in BADGES.items():
            if flags & badge_flag == badge_flag:
                badges.append(badge_name)

        return badges

with open('resultados.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badges(temp)
            if len(z) != 0:
                badges = ', '.join(z)
                print(f'ID: <@{id}> | Nome de usuário: {username} | Badges: {badges} | Data de criação: {creation_date}')
                file.write(f'ID: <@{id}> | Nome de usuário: {username} | Badges: {badges}\n')
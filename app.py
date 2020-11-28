import discord
from discord.ext import commands
from discord.abc import PrivateChannel
import os
import random
import asyncio
import time
import datetime
import requests
import glob


from PIL import Image, ImageOps, ImageDraw, ImageFilter

from io import BytesIO

HelloList = ["coucou","salut","yo","eyh","hey","hello","bonjour","slt"]
ByeList = ["bye","a+","@+","au revoir","adieu","tchao","tcho","a la prochaine","bonne nuit","bonne journée","hasta la bista","adios"]

prefix = "_"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, description="Welcome, type "+prefix+"infos")


@bot.event
async def on_ready():
	print("Le bot a démarré.")
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="say hello to Mme. Astie"))

#La commande de test
@bot.command()
async def test(ctx):
	'''
	with open('tr.js', 'rb') as fh:
		f = discord.File(fh, filename='tr.js')
		
	await ctx.send(file=f)
	'''
'''
'''
class CoursLycée(commands.Cog):
	global checkFakeSubcommand
	async def checkFakeSubcommand(self, ctx):
		count = -2
		for arg in ctx.message.content.split(" "):
			count += 1	
		if count >= 0:
			embed = discord.Embed(title="Sous commande inconnu !", colour=discord.Colour(0xed1f20))
			await ctx.send(embed=embed)
			return True
		else:
			return False
	global checkFakeSubSubcommand
	async def checkFakeSubSubcommand(self, ctx):
		count = -3
		for arg in ctx.message.content.split(" "):
			count += 1	
		if count >= 0:
			embed = discord.Embed(title="Sous commande inconnu !", colour=discord.Colour(0xed1f20))
			await ctx.send(embed=embed)
			return True
		else:
			return False

	@commands.group(brief="Affiche la totalité des cours vu en NSI", invoke_without_command=True)
	@commands.guild_only()
	async def cours(self, ctx):
		global checkFakeSubcommand
		if await checkFakeSubcommand(self, ctx) == False:
			file = discord.File("logo.png", filename="logo.png")

			embed = discord.Embed(title="Retrouves ici la totalité des cours de NSI !", colour=discord.Colour(0x4259), description="Toutes les catégories mise à part \"Approfondir\" ont été vues en cours.", timestamp=datetime.datetime.now())
			embed.set_footer(text="Message généré par "+str(ctx.author), icon_url="attachment://logo.png")
			embed.add_field(name="Python", value="Pour accèder au cours python, Envoi `"+prefix+"cours python` !", inline=False)
			embed.add_field(name="Bases", value="Pour voir les cours sur les bases (2,4,10,16, etc..), Envoi `"+prefix+"cours bases` !", inline=False)
			embed.add_field(name="Von Neumann", value="Pour voir les cours sur l'architecture de Von Neumann, Envoi `"+prefix+"cours neumann` !", inline=False)
			embed.add_field(name="Assembleur", value="Pour accèder au cours sur l'assembleur, Envoi `"+prefix+"cours assembleur` !", inline=False)
			embed.add_field(name="Approfondir", value="Pour accèder à des contenus supplémentaires, Envoi `"+prefix+"cours supp` !", inline=True)
			embed.add_field(name="Facts", value="Pour lire des faits sur les cours, Envoi `"+prefix+"cours fact` !", inline=True)

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()


	'''
	' Python command
	'''
	@cours.group(brief="Affiche la totalité des cours Python vu en NSI", invoke_without_command=True)
	@commands.guild_only()
	async def python(self, ctx):
		global checkFakeSubSubcommand
		if await checkFakeSubSubcommand(self, ctx) == False:
			file = discord.File("logo.png", filename="logo.png")

			embed = discord.Embed(title="Retrouves ici la totalité des cours Python réalisé en NSI !", colour=discord.Colour(0x4259), description="Toutes les catégories ont été vues en cours.", timestamp=datetime.datetime.now())
			embed.set_footer(text="Message généré par "+str(ctx.author), icon_url="attachment://logo.png")
			embed.add_field(name="Types :", value="Pour accèder au cours sur les types (str, int, etc..), Envoi `"+prefix+"cours python types` !", inline=False)
			embed.add_field(name="Conversions :", value="Pour voir les cours sur conversions entre tables, Envoi `"+prefix+"cours python conversions` !", inline=False)
			embed.add_field(name="Listes :", value="Pour voir les cours sur les listes, Envoi `"+prefix+"cours python listes` !", inline=False)
			embed.add_field(name="Dictionnaires :", value="Pour accèder au cours sur les dictionnaires, Envoi `"+prefix+"cours python dictionnaires` !", inline=False)
				
			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
	
	#Python subcommand
	@python.command(brief="Affiche les cours sur les types en python")
	async def types(self, ctx):

		embed = discord.Embed(title="Les différents types dans python")
		embed.add_field(name="Les chaînes de caractères" ,value="Réponds par `str`", inline=False)
		embed.add_field(name="Les nombres" ,value="Réponds par `numbers`", inline=False)
		embed.add_field(name="Les booléens" ,value="Réponds par `bool`", inline=False)
		await ctx.message.author.send(embed=embed)

		async def publicMsg(self, ctx):
			#Public message
			url = ctx.message.author.avatar_url
			r = requests.get(url, allow_redirects=False)
			open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

			file = discord.File(str(ctx.message.author.id)+'.png', filename=str(ctx.message.author.id)+'.png')
			embed = discord.Embed(title="Les cours sur les types viennent de t'être envoyé !", colour=discord.Colour(0x4259), timestamp=datetime.datetime.now())
			embed.set_footer(text="Cours demandé par "+str(ctx.author), icon_url="attachment://"+str(ctx.message.author.id)+".png")

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
			os.remove(str(ctx.message.author.id)+".png")
		await publicMsg(self, ctx)
	#Python subcommand
	@python.command(brief="Affiche les cours sur les conversions en python")
	async def conversions(self, ctx):

		embed = discord.Embed(title="Les différentes conversions en python")
		embed.add_field(name="Conversions entre types" ,value="Réponds par `types`", inline=False)
		embed.add_field(name="Conversions entre les tables" ,value="Réponds par `tables`", inline=False)
		await ctx.message.author.send(embed=embed)

		async def publicMsg(self, ctx):
			#Public message
			url = ctx.message.author.avatar_url
			r = requests.get(url, allow_redirects=False)
			open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

			file = discord.File(str(ctx.message.author.id)+'.png', filename=str(ctx.message.author.id)+'.png')
			embed = discord.Embed(title="Les cours sur les conversions viennent de t'être envoyé !", colour=discord.Colour(0x4259), timestamp=datetime.datetime.now())
			embed.set_footer(text="Cours demandé par "+str(ctx.author), icon_url="attachment://"+str(ctx.message.author.id)+".png")

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
			os.remove(str(ctx.message.author.id)+".png")
		await publicMsg(self, ctx)
	#Python subcommand
	@python.command(brief="Affiche les cours sur les listes en python")
	async def listes(self, ctx):

		embed = discord.Embed(title="Les listes en python")
		embed.add_field(name="Les listes simple" ,value="Réponds par `listes`", inline=False)
		embed.add_field(name="Les listes dictionnaires" ,value="Réponds par `dictionnaires`", inline=False)
		await ctx.message.author.send(embed=embed)

		async def publicMsg(self, ctx):
			#Public message
			url = ctx.message.author.avatar_url
			r = requests.get(url, allow_redirects=False)
			open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

			file = discord.File(str(ctx.message.author.id)+'.png', filename=str(ctx.message.author.id)+'.png')
			embed = discord.Embed(title="Les cours sur les listes viennent de t'être envoyé !", colour=discord.Colour(0x4259), timestamp=datetime.datetime.now())
			embed.set_footer(text="Cours demandé par "+str(ctx.author), icon_url="attachment://"+str(ctx.message.author.id)+".png")

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
			os.remove(str(ctx.message.author.id)+".png")
		await publicMsg(self, ctx)
	#Python subcommand
	@python.command(brief="Affiche les cours sur les dictionnaires en python")
	async def dictionnaires(self, ctx):

		embed = discord.Embed(title="Les dictionnaires en python")
		embed.add_field(name="Les dictionnaires" ,value="Réponds par `dictionnaires`", inline=False)
		await ctx.message.author.send(embed=embed)

		async def publicMsg(self, ctx):
			#Public message
			url = ctx.message.author.avatar_url
			r = requests.get(url, allow_redirects=False)
			open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

			file = discord.File(str(ctx.message.author.id)+'.png', filename=str(ctx.message.author.id)+'.png')
			embed = discord.Embed(title="Les cours sur les dictionnaires viennent de t'être envoyé !", colour=discord.Colour(0x4259), timestamp=datetime.datetime.now())
			embed.set_footer(text="Cours demandé par "+str(ctx.author), icon_url="attachment://"+str(ctx.message.author.id)+".png")

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
			os.remove(str(ctx.message.author.id)+".png")
		await publicMsg(self, ctx)


	'''
	' Binary command
	'''
	@cours.group(invoke_without_command=True)
	@commands.guild_only()
	async def bases(self, ctx):
		global checkFakeSubSubcommand
		if await checkFakeSubSubcommand(self, ctx) == False:
			file = discord.File("logo.png", filename="logo.png")

			embed = discord.Embed(title="Retrouves ici la totalité des cours sur les bases réalisé en NSI !", colour=discord.Colour(0x4259), description="Toutes les catégories ont été vues en cours.", timestamp=datetime.datetime.now())
			embed.set_footer(text="Message généré par "+str(ctx.author), icon_url="attachment://logo.png")
			embed.add_field(name="Base 2", value="Pour accèder au cours sur le binaire, Envoi `"+prefix+"cours bases two` !", inline=False)
			embed.add_field(name="Base 4", value="Pour voir les cours sur le système quaternaire, Envoi `"+prefix+"cours bases four` !", inline=False)
			embed.add_field(name="Base 8", value="Pour voir les cours sur le système octal, Envoi `"+prefix+"cours bases eight` !", inline=False)
			embed.add_field(name="Base 10", value="Pour voir les cours sur le système décimal, Envoi `"+prefix+"cours bases ten` !", inline=False)
			embed.add_field(name="Base 16", value="Pour voir les cours sur le système hexadécimal, Envoi `"+prefix+"cours bases sixteen` !", inline=False)
			embed.add_field(name="Base 32", value="Pour voir les cours sur le système de base 32, Envoi `"+prefix+"cours bases thirthytwo` !", inline=False)
			embed.add_field(name="Base 64", value="Pour voir les cours sur le système de base 64, Envoi `"+prefix+"cours bases sixtyfour` !", inline=False)
				
			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
	
	#Bases subcommand
	@bases.command(brief="Cours sur le binaire")
	@commands.guild_only()
	async def two(self, ctx):

		embed = discord.Embed(title="Le binaire")
		embed.add_field(name="Fonctionnement" ,value="Bla bla bla", inline=False)
		embed.add_field(name="Usage" ,value="Bla bla bla", inline=False)
		embed.add_field(name="Conversion" ,value="Envoi `tables` !", inline=False)
		await ctx.message.author.send(embed=embed)

		async def publicMsg(self, ctx):
			#Public message
			url = ctx.message.author.avatar_url
			r = requests.get(url, allow_redirects=False)
			open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

			file = discord.File(str(ctx.message.author.id)+'.png', filename=str(ctx.message.author.id)+'.png')
			embed = discord.Embed(title="Les cours sur le binaire viennent de t'être envoyé !", colour=discord.Colour(0x4259), timestamp=datetime.datetime.now())
			embed.set_footer(text="Cours demandé par "+str(ctx.author), icon_url="attachment://"+str(ctx.message.author.id)+".png")

			await ctx.send(file=file, embed=embed)
			await ctx.message.delete()
			os.remove(str(ctx.message.author.id)+".png")
		await publicMsg(self, ctx)
	'''
	' Von Neumann command
	'''
	@cours.group(invoke_without_command=True)
	@commands.guild_only()
	async def neumann(self, ctx):

		await ctx.send("Voici les cours sur l'architecture de Von Neumann sa mère")

	
	'''
	' Assembly command
	'''
	@cours.group(invoke_without_command=True)
	@commands.guild_only()
	async def assembleur(self, ctx):

		await ctx.send("Voici les cours sur l'assembleur sa mère")

	
	'''
	' More class command
	'''
	@cours.group(invoke_without_command=True)
	@commands.guild_only()
	async def supp(self, ctx):

		await ctx.send("Pas de cours supplémentaires disponible pour le moment..")
	

	'''
	' Facts command
	'''
	@cours.group(invoke_without_command=True)
	@commands.guild_only()
	async def fact(self, ctx):

		await ctx.send("Pas de facts disponible pour le moment..")
'''
'''
class RandomAndUselessThings(commands.Cog):
	@commands.command(category="Random/Useless", brief="Vous dit bonjour")
	async def hello(self, ctx):

		await ctx.send("Salut <@"+str(ctx.author.id)+"> !")

	@commands.command(category="Random/Useless", brief="Dites bonjour à quelqu'un !")
	@commands.guild_only()
	async def helloYou(self, ctx, arg):
		await ctx.message.delete()
		await ctx.send("Salut "+str(arg)+" !")

	@commands.command()
	async def money(self, ctx):
		await ctx.message.author.send("👋 Hey! Je t'envoie 5 € en cadeau sur ta carte Zelf.\nZelf te propose des services pour payer ultra-rapidement, et fonctionne avec les messageries.\n⚡️Envoie et reçois de l'argent facilement par SMS ou par commande vocale, sans frais.\nRejoins-moi et obtiens ton bonus de 5 € ici 👇😉\nhttps://zelf.co/s/SLPARWRMRK")
		embed = discord.Embed(title="Je t'ai envoyé 5€ en dm !", colour=discord.Color(0xe))
		await ctx.send(embed=embed)

class Modération(commands.Cog):
	@commands.command(brief="Supprime le nombre de messages indiqué (200max)", aliases=['del', 'clean'])
	@commands.guild_only()
	async def clear(self, ctx, arg):
		if arg.isdigit() == False:
			await ctx.send("**" + str(arg) + "** n'est pas un nombre valide. Veuillez spécifier un nombre de messages à supprimer.")
		else:
			await ctx.send('Clear started. It can have some delays between clears.')
			await asyncio.sleep(1.5)
			async for msg in ctx.channel.history(limit=int(arg)+2):
				await msg.delete()
				await asyncio.sleep(0.5)

	@commands.command(brief="Supprime 200 messages", aliases=['purge','cls', 'cleanall'])
	@commands.guild_only()
	async def clearall(self, ctx):
		await ctx.send('Clearing messages... (The limit is about 200msgs deleted at one time')
		await asyncio.sleep(1.5)
		async for msg in ctx.channel.history():
			await msg.delete()
			await asyncio.sleep(0.5)

	@commands.command(brief="Créer un channel avec le nom fourni", aliases=['cc','ccreate'])
	@commands.guild_only()
	async def createChannel(self, ctx, arg):
		await ctx.guild.create_text_channel(arg)
		
		channel = discord.utils.get(ctx.guild.channels, name=arg)
		await ctx.send("Le channel <#"+str(channel.id)+"> vient d'être créé")

	@commands.command(brief="Supprime le channel indiqué", aliases=['dc','cdelete'])
	@commands.guild_only()
	async def deleteChannel(self, ctx, arg):
		existing_channel = discord.utils.get(ctx.guild.channels, name=arg)
		await existing_channel.delete()

		await ctx.send("Le channel #"+str(existing_channel)+" vient d'être supprimé")

	@commands.command(brief="Créer un rôle avec le nom et les permissions donnés", aliases=['cr', 'rolecreate'])
	@commands.guild_only()
	async def createRole(self, ctx, arg):
		perms = discord.Permissions(send_messages=True, read_messages=True,manage_guild=True,administrator=True,manage_messages=True,manage_roles=True,manage_permissions=True,manage_webhooks=True,manage_emojis=True)
		await ctx.guild.create_role(name=arg, permissions=perms)

		role = discord.utils.get(ctx.message.author.guild.roles, name=arg)
		await ctx.send("Le rôle "+str(role)+" a bien été créé")

	@commands.command(brief="Modifie le rôle indiqué avec les permissions donnés", description="Vous devez utiliser cette commande de telle sorte à définir les 34 permissions de rôle. Les rôles sont dans cette ordre:\n create_instant_invite\n kick_members\n ban_members\n administrator\n manage_channels\n manage_guild\n add_reactions\n view_audit_log\n priority_speaker\n stream\n read_messages\n view_channel\n send_messages\n send_tts_messages\n manage_messages\n embed_links\n attach_files\n read_message_history\n mention_everyone\n external_emojis\n use_external_emojis\n view_guild_insights\n connect\n speak\n mute_members\n deafen_members\n move_members\n use_voice_activation\n change_nickname\n manage_nicknames\n manage_roles\n manage_permissions\n manage_webhooks\n manage_emojis\n \nVous devez indiquer \"True\" pour accorder la permission et \"False\" pour la refuser.", aliases=['mr', 'rolemodify', 'editrole', 'er'])
	@commands.guild_only()
	async def modifRole(self, ctx, arg, *, args):

		#On sépare chaque mots un à un
		argsList = args.split(' ')
		#On les mets dans une liste
		permsList = list(argsList)

		#On vérifie qu'on a bien nos 34 valeur de perms
		if len(permsList) != 34:
			#Sinon, on préviens qu'il en manque
			await ctx.send("Erreur: Il manque "+str(len(argsList))-34)+" permissions à définir"
		else:
			#On crée la fonction pour retourner un BOOL et non un STR
			def func(arg):
				if permsList[int(arg)] == "True":
					return True
				elif permsList[int(arg)] == "False":
					return False

			user = ctx.message.author
			role = discord.utils.get(user.guild.roles, name=arg)

			perms = discord.Permissions()
			perms.update(create_instant_invite=func(0),kick_members=func(1),ban_members=func(2),administrator=func(3),manage_channels=func(4),manage_guild=func(5),add_reactions=func(6),view_audit_log=func(7),priority_speaker=func(8),stream=func(9),read_messages=func(10),view_channel=func(11),send_messages=func(12),send_tts_messages=func(13),manage_messages=func(14),embed_links=func(15),attach_files=func(16),read_message_history=func(17),mention_everyone=func(18),external_emojis=func(19),use_external_emojis=func(20),view_guild_insights=func(21),connect=func(22),speak=func(23),mute_members=func(24),deafen_members=func(25),move_members=func(26),use_voice_activation=func(27),change_nickname=func(28),manage_nicknames=func(29),manage_roles=func(30),manage_permissions=func(31),manage_webhooks=func(32),manage_emojis=func(33))

			await role.edit(reason="Requested by"+str(ctx.message.author), permissions=perms)	
			await ctx.send("Le rôle "+str(role)+" a bien été modifié")		

	@commands.command(brief="Supprime le rôle indiqué")
	@commands.guild_only()
	async def deleteRole(self, ctx, arg : discord.Role):
		await ctx.guild.delete_role(name=arg)
		await ctx.send("Le rôle "+str(arg)+" a bien été supprimé")

class ModificationImages(commands.Cog):
	@commands.command(brief="Ajoute un petit copyright sur vos images !", description="Attention, la transparence n'est pas prise en charge !", aliases=['©'])
	@commands.guild_only()
	async def copyright(self, ctx):
		url = ctx.message.attachments[0].url
		r = requests.get(url, allow_redirects=False)
		open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

		bg = Image.open(str(ctx.message.author.id)+".png").convert('RGB')
		widthbg, heightbg = bg.size
		fg = Image.open('copyright.png').convert('RGBA')

		bg.paste(fg, box=(widthbg-105, heightbg-52), mask=fg)
		bg.save('result.jpg')

		fg.close()
		bg.close()

		with open('result.jpg', 'rb') as fh:
			f = discord.File(fh, filename='result.jpg')
		
		embed = discord.Embed(title="L'image a bien été copyrighté !", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
		embed.set_image(url="attachment://result.jpg")
		embed.set_footer(text="Effectué par "+str(ctx.message.author)+" !")
		
		await ctx.send(embed=embed, file=f)
		await ctx.message.delete()

		fh.close()

		os.remove("result.jpg")
		os.remove(str(ctx.message.author.id)+".png")
	
	@commands.command(brief="Rajoute un effet varicelle sur tes images !", description="Attention la transparence n'est pas prise en charge !")
	@commands.guild_only()
	async def varicelle(self, ctx, arg):
		
		url = ctx.message.attachments[0].url
		r = requests.get(url, allow_redirects=False)
		open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

		img = Image.open(str(ctx.message.author.id)+'.png')
		width, height = img.size

		if int(arg) == 1:
			val = 1000
		elif int(arg) == 2:
			val = 800
		elif int(arg) == 3:
			val = 700
		elif int(arg) == 4:
			val = 600
		elif int(arg) == 5:
			val = 500
		elif int(arg) == 6:
			val = 400
		elif int(arg) == 7:
			val = 300
		elif int(arg) == 8:
			val = 200
		elif int(arg) == 9:
			val = 100
		elif int(arg) == 10:
			val = 10

		for i in range(int((width*height)/int(val))):
			x = random.randint(1, width-1)
			y = random.randint(1, height-1)

			img.putpixel((x,y), (255,0,0))

		
		img.save('result.png')
		img.close()

		with open('result.png', 'rb') as fr:
			f = discord.File(fr, filename='result.png')
		with open(str(ctx.message.author.id)+'.png', 'rb') as fo:
			f2 = discord.File(fo, filename=str(ctx.message.author.id)+'.png')

		embed = discord.Embed(title="L'original", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
		embed.set_footer(text="Image envoyé par "+str(ctx.author))
		embed.set_image(url="attachment://"+str(ctx.message.author.id)+'.png')
		
		await ctx.send(file=f2, embed=embed)

		embed = discord.Embed(title="Le nouveau", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
		embed.set_image(url="attachment://result.png")

		await ctx.send(file=f, embed=embed)
		await ctx.message.delete()

		fr.close()
		fo.close()
		os.remove(str(ctx.message.author.id)+'.png')
		os.remove("result.png")
	
	@commands.command(brief="Passe ton image en négatif pour un effet flippant !", description="Attention la transparence n'est pas prise en charge !", aliases=['negative'])
	@commands.guild_only()
	async def negatif(self, ctx):
	
		url = ctx.message.attachments[0].url
		r = requests.get(url, allow_redirects=False)
		open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)

		img = Image.open(str(ctx.message.author.id)+'.png')
		width, height = img.size

		img = Image.open(str(ctx.message.author.id)+'.png').convert('RGB')
		img_invert = ImageOps.invert(img)
		img_invert.save('result.png')
		img.close()


		with open('result.png', 'rb') as fr:
			f = discord.File(fr, filename='result.png')
		with open(str(ctx.message.author.id)+'.png', 'rb') as fo:
			f2 = discord.File(fo, filename=str(ctx.message.author.id)+'.png')

		embed = discord.Embed(title="L'original", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
		embed.set_footer(text="Image envoyé par "+str(ctx.author))
		embed.set_image(url="attachment://"+str(ctx.message.author.id)+'.png')
		
		await ctx.send(file=f2, embed=embed)


		embed = discord.Embed(title="Le nouveau", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
		embed.set_image(url="attachment://result.png")

		await ctx.send(file=f, embed=embed)

		await ctx.message.delete()

		img_invert.close()
		fr.close()
		fo.close()
		os.remove(str(ctx.message.author.id)+'.png')
		os.remove("result.png")

	@commands.command(brief="Fait circuler ton image sur un gif !", description="Attention la transparence n'est pas prise en charge, plus l'image est grande, moins elle circulera")
	@commands.guild_only()
	async def gif(self, ctx):
		url = ctx.message.attachments[0].url
		r = requests.get(url, allow_redirects=False)
		open(str(ctx.message.author.id)+'.png', 'wb').write(r.content)
		
		img = Image.open(str(ctx.message.author.id)+'.png')
		width, height = img.size
		img.close()

		names = ['img{:2d}.gif'.format(i) for i in range(51)]
		# Create the individual frames as png images
		im = Image.new("RGBA", (width+500, height), (54,57,63))

		pos = 0
		pos2 = 0


		images = []

		for n in names:
			def color():
				color = "%06x" % random.randint(0, 0xFFFFFF)
				return '#'+str(color)
			frame = im.copy()
			img = Image.open(str(ctx.message.author.id)+'.png')
			frame.paste(img, (pos, pos2))
			frame.save(n)
			pos += 10
			pos2 += 0

		for n in names:
		    frame = Image.open(n)
		    images.append(frame)

		# Save the frames as an animated GIF
		images[0].save(str(ctx.message.author.id)+'.gif',
		               save_all=True,
		               append_images=images[1:],
		               duration=50,
		               loop=0)
				

		with open(str(ctx.message.author.id)+'.gif', 'rb') as fg:
			f = discord.File(fg, filename=str(ctx.message.author.id)+'.gif')

		await ctx.send(file=f)
		fg.close()
		im.close()
		img.close()
		frame.close()
		os.remove(str(ctx.message.author.id)+'.gif')
		os.remove(str(ctx.message.author.id)+'.png')

		i = 0
		for loop in range(10):
			images[int(i)].close()
			os.remove("img "+str(i)+".gif")
			i += 1

		i = 10
		for loop in range(41):
			images[int(i)].close()
			os.remove("img"+str(i)+".gif")
			i += 1

class ModificationServeur(commands.Cog):
	@commands.command(category="Modification du serveur", brief="Remplace le logo du serveur par l'image jointe !")
	@commands.guild_only()
	async def changeServLogo(self, ctx):
		url = ctx.message.attachments[0].url
		r = requests.get(url, allow_redirects=False)
		open('ServerLogo.png', 'wb').write(r.content)
		
		with open('ServerLogo.png', 'rb') as f:
			icon = f.read()
			file = discord.File("ServerLogo.png", filename="ServerLogo.png")

			await ctx.message.guild.edit(icon=icon)

			embed = discord.Embed(title="L'icone du serveur vient d'être changer !", colour=discord.Colour(0xe), timestamp=datetime.datetime.now())
			embed.set_image(url="attachment://ServerLogo.png")
			embed.set_footer(text="Effectué par "+str(ctx.message.author)+" !")
			await ctx.send(file=file, embed=embed)

		await ctx.message.delete()
		os.remove("ServerLogo.png")

class InformationsMembres(commands.Cog):
	@commands.command(brief="Obtient la photo de profil de quelqu'un")
	@commands.guild_only()
	async def pdp(self, ctx, arg : discord.Member=None):
		await ctx.send("Voici la pdp de "+str(arg)+" !")
		await ctx.send(arg.avatar_url)

	@commands.command(brief="Obtient des infos sur quelqu'un")
	@commands.guild_only()
	async def infos(self, ctx, arg : discord.Member=None):

		await ctx.send("Compte crée le `"+str(arg.created_at)+"`")

class InformationsBot(commands.Cog):	
	@commands.command(category="Informations sur le bot", brief="Infos sur le bot")
	async def informations(self, ctx):
		file = discord.File("logo.png", filename="logo.png")
		embed = discord.Embed(colour=discord.Colour(0x17bc5f))
		embed.set_thumbnail(url="attachment://logo.png")
		embed.set_author(name="NSI's Discord bot", url="http://pastebin.fr/72976", icon_url="https://cdn.discordapp.com/avatars/776812266048716804/9193825923bd89b21d1f00350c549dbd.png")
		embed.set_footer(text="Gaëtan is a good developer nah?", icon_url="https://ghrlt.fr/",)
		embed.add_field(name="Informations", value="Ce bot est développé par Gaëtan (for yet), dans le cadre des cours Python en NSI", inline=False)
		embed.add_field(name="Utilité", value="S'exercer en Python, proposer les exercices fait en cours, maybe a \"Daily learn\"", inline=False)
		embed.add_field(name="Commandes", value="_help", inline=True)
		embed.add_field(name="Don", value="Come in my pm", inline=True)

		await ctx.send(file=file, embed=embed)

class SafeForSchool(commands.Cog):
	@commands.command(brief="Génére une blague random")
	@commands.guild_only()
	async def jokes(self, ctx):
		req = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
		await ctx.send("`"+req.json()['joke']+"`")


bot.add_cog(CoursLycée(bot))

bot.add_cog(RandomAndUselessThings(bot))
bot.add_cog(Modération(bot))
bot.add_cog(ModificationImages(bot))
bot.add_cog(ModificationServeur(bot))
bot.add_cog(InformationsMembres(bot))
bot.add_cog(InformationsBot(bot))
bot.add_cog(SafeForSchool(bot))

'''
' '
'''

@bot.event
async def on_message(message):
	if message.author.id != 776812266048716804:
		for word in HelloList:
			if word in message.content.lower():
				await message.add_reaction("👋")
		for word in ByeList:
			if word in message.content.lower():
				await message.add_reaction("🤙")

	if isinstance(message.channel, PrivateChannel) == True:
		if message.author != bot.user:
			#''' Python Types '''
			if message.content == "str":
				await message.channel.send("String")
			elif message.content == "numbers":
				await message.channel.send("Integers, Floating point number, complex")
			elif message.content == "bool":
				await message.channel.send("Boolean")
			
			#''' Python Conversions '''
			elif message.content == "types":
				await message.channel.send("Conversions entre types")
			elif message.content == "tables":
				await message.channel.send("Conversions entre tables")

			#''' Python Listes '''
			elif message.content == "listes":
				await message.channel.send("https://python.sdv.univ-paris-diderot.fr/04_listes/")
			#Pour les dictionnaires, on se référe à juste en desous

			#''' Python Dictionnaires '''
			elif message.content == "dictionnaires":
				await message.channel.send("https://python.sdv.univ-paris-diderot.fr/13_dictionnaires_tuples_sets/")
			#''' NSFW '''
			elif message.content == "porn":
				import pornhub

				client = pornhub.PornHub()

				for video in client.getVideos(1,page=1):
					url = video['background']
					r = requests.get(url, allow_redirects=False)
					open(str(video['rating'])+str(message.author.id)+'.jpg', 'wb').write(r.content)

					with open(str(video['rating'])+str(message.author.id)+'.jpg', 'rb') as fh:
						f = discord.File(fh, filename=str(video['rating'])+str(message.author.id)+'.jpg')
				
					embed = discord.Embed(title=str(video['name']), description="[Voir la vidéo]("+str(video['url'])+")")
					embed.set_image(url='attachment://'+str(video['rating'])+str(message.author.id)+'.jpg')
					embedPrevention = discord.Embed(title="Attention, du contenu potentiellement pornographique va apparaître. Souhaitez-vous continuer ?", color=discord.Colour(0xed1f20))
					await message.author.send(embed=embedPrevention)
					await bot.wait_for('message', check=lambda message : message.content == "oui")
					print(message.author+" is horny")
					await message.author.send(file=f, embed=embed)

					fh.close()
					os.remove(str(video['rating'])+str(message.author.id)+'.jpg')
			elif message.content == "oui":
				response = True
			elif message.content == "non":
				response = False
			#Command didn't exist or non usable on dm
			else:
				embed = discord.Embed(title="Cette commande n'existe pas ou bien n'est pas utilisable en mp !", color=discord.Colour(0xed1f20))
				await message.channel.send(embed=embed)
		else:
			pass
	else:
		pass

	await bot.process_commands(message)
bot.run('Nzc2ODEyMjY2MDQ4NzE2ODA0.X66UzA.i5cPLzn6nFTuBRs-skpM2PakW-4')

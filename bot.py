import discord
import random
from replit import db
from discord.ext import commands
from keep_alive import keep_alive



quotes_database = ["Make the lie big. Make it simple. Keep saying it, and eventually people will believe it.", "Death is the solution to all problems. No man, no problem.", "You cannot run faster than a bullet.", "There is no state with a democracy except Libya on the whole planet.", "Politics is when you say you are going to do one thing while intending to do another. Then you do neither what you said, nor what you intended.", "Do not compare yourself to others. If you do so, you’re insulting yourself.", "North Americans don’t understand that our country is not just Cuba; our country is also humanity.", "Ideas are more powerful than guns. We would not let our enemies have guns. Why should we let them have ideas?", "He alone, who owns the youth, gains the future.", "Let us have a dagger between our teeth, a bomb in our hands, and an infinite scorn in our hearts.", "I use emotion for the many and reserve reason for the few.", "The oppressed peoples can liberate themselves only through struggle. This is a simple and clear truth confirmed by history.", "I want you to know that everything I did, I did for my country.", "Sorry, I’m still a dialectical materialist.", "The modern revisionists and reactionaries call us Stalinists, thinking that they insult us and, in fact, that is what they have in mind. But, on the contrary, they glorify us with this epithet; it is an honor for us to be Stalinists for while we maintain such a stand the enemy cannot and will never force us to our knees.", "The problem with socialism is that you eventually run out of other people's money.", "There is no difference between communism and socialism, except in the means of achieving the same ultimate end: communism proposes to enslave men by force, socialism -- by vote. It is merely the difference between murder and suicide.", "We think too small, like the frog at the bottom of the well. He thinks the sky is only as big as the top of the well. If he surfaced, he would have an entirely different view.", "Many will call me an adventurer, and that I am...only one of a different sort: one who risks his skin to prove his truths."]

rapper_names = ["-50 Cent", "-Eminem", "-Kanye West", "-Snoop Dogg", "-Tupac", "-DaBaby", "-Kim Kardashian", "-Billie Eilish", "-Charli Damelio", "-Ash Ketchum", "-Drake", "-Jay-Z", "-Kendrick Lamar"]


def update_quotes(quotes_message):
  if "quotes" in db.keys():
    quotes = db["quotes"]
    quotes.append(quotes_message)
    db["quotes"] = quotes
  else:
    db["quotes"] = [quotes_message]

def delete_quote(index):
  quotes = db["quotes"]
  if len(quotes) > index:
    del quotes[index]
  db["quotes"] = quotes



client = commands.Bot(command_prefix = "!")







@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))






@client.event
async def on_message(message):
  if message.author == client.user:
    return

  options = quotes_database
  if "quotes" in db.keys():
    options = options + db["quotes"]
  
  if message.content.startswith(('!quote')):
    await message.channel.send(random.choice(options))
  if message.content.startswith(('!quote')):
    await message.channel.send(random.choice(rapper_names))
  if message.content.startswith('Vaush'):
    await message.channel.send('Lol Vaushite')
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

  
  
  if message.content.startswith("!newquote"):
    quotes_message = message.content.split("!newquote ",1)[1]
    update_quotes(quotes_message)
    await message.channel.send("New quote added.")
  
  if message.content.startswith("!delquote"):
    quotes = []
    if "quotes" in db.keys():
      index = int(message.content.split("!delquote",1)[1])
      delete_quote(index)
      quotes = db["quotes"]
    await message.channel.send(quotes)

  if message.content.startswith("!list"):
    quotes = []
    if "quotes" in db.keys():
      quotes = db["quotes"]
    await message.channel.send(quotes)


keep_alive()
client.run(TOKEN)

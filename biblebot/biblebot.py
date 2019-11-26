import discord
client = discord.Client()
token = open('token.txt', 'r').read()
books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1Samuel', '2Samuel', '1Kings', '2Kings', '1Chronicles', '2Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalm', 'Proverbs', 'Ecclesiastes', 'Songofsolomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1Corinthians', '2Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1Thessalonians', '2Thessalonians', '1Timothy', '2Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1Peter', '2Peter', '1John', '2John', '3John', 'Jude', 'Revelation']
@client.event
async def on_connect():
    print('{} has been connected'.format(client.user))
@client.event
async def on_ready():
    print('{} is now ready to use!'.format(client.user))
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        if not message.mention_everyone:
            await message.channel.send("Allow me to introduce myself. I am BibleBot. Do `!bible Genesis 1:1` to find verses and `!biblehelp` for more info")
    if message.content == '!bible':
        await message.channel.send('You need to input a book and verse! Type `!biblehelp` for more info!')
    if message.content.startswith('!bible '):
        for x in books:
            try:
                if message.content.index(x):
                    filechoosen = x.lower()
                    filechoosen = filechoosen+ 'verses'
                    filechoosen = filechoosen + '.txt'
                    good = 0
                    if message.content == '!bible' + ' {}'.format(x):
                        await message.channel.send('You need to input a verse!')
                        good += 1
                    try:    
                        book = open(filechoosen, 'r').read()
                        book = book.split('|')
                    except:
                        await message.channel.send("I'm sorry, I have not added this book yet. I only have Genesis to Ephesians")
                        good += 1
                    verse = message.content.replace('!bible ', '')
                    verse = verse.replace(x + " ", '')
                    for i in book:
                        if i.__contains__('{} {} '.format(x, verse)):
                            await message.channel.send(i)
                            good += 1
                    if good == 0:
                        await message.channel.send('Verse not found')
            except:
                pass
        a = 0
        while a < len(books):
            a += 1
            b = str(a)
            try:
                if message.content == '!bible' + ' {}'.format(b):
                    await message.channel.send('You need to input a verse!')
                if message.content.index(b + ' '):
                    print('good')
                    book = a - 1
                    book = books[book]
                    print(book)
                    tempbible = book
                    filechoosen = book.lower()
                    filechoosen = filechoosen+ 'verses'
                    filechoosen = filechoosen + '.txt'
                    verse = message.content.replace('!bible ' + b, '')
                    print(verse)
                    #verse = verse.replace(b + ' ', '')
                    verse = verse.strip()
                    print(verse)
                    print(filechoosen)
                    good = 0
                    try:      
                        book = open(filechoosen, 'r').read()
                        book = book.split('|')
                    except:
                        await message.channel.send("I'm sorry, I have not added this book yet. I only have Genesis to Ephesians")
                        good += 1
                        break
                    for i in book:
                        if i.__contains__('{} {} '.format(tempbible, verse)):
                            print('yes')
                            await message.channel.send(i)
                            good += 1
                    if good == 0:
                        if not ' ' in verse:
                            await message.channel.send('Verse not found')
            except:
                pass
    if message.content.startswith('!books'):
        page = message.content.replace('!books', '')
        page = page.strip()
        print(page)
        if page == '1' or page == '':    
            bookembed = discord.Embed(title="Books", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="1", value="Genesis", inline=True)
            bookembed.add_field(name="2", value="Exodus", inline=True)
            bookembed.add_field(name="3", value="Leviticus", inline=True)
            bookembed.add_field(name="4", value="Numbers", inline=True)
            bookembed.add_field(name="5", value="Deuteronomy", inline=True)
            bookembed.add_field(name="6", value="Joshua", inline=True)
            bookembed.set_footer(text = 'Type !books 2 to continue')
            await message.channel.send(embed=bookembed)
        if page == '2':    
            bookembed = discord.Embed(title="Books 2", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="7", value="Judges", inline=True)
            bookembed.add_field(name="8", value="Ruth", inline=True)
            bookembed.add_field(name="9", value="1Samuel", inline=True)
            bookembed.add_field(name="10", value="2Samuel", inline=True)
            bookembed.add_field(name="11", value="1Kings", inline=True)
            bookembed.add_field(name="12", value="2Kings", inline=True)
            bookembed.set_footer(text = 'Type !books 3 to continue')
            await message.channel.send(embed=bookembed)
        if page == '3':    
            bookembed = discord.Embed(title="Books 3", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="13", value="1Chronicles", inline=True)
            bookembed.add_field(name="14", value="2Chronicles", inline=True)
            bookembed.add_field(name="15", value="Ezra", inline=True)
            bookembed.add_field(name="16", value="Nehemiah", inline=True)
            bookembed.add_field(name="17", value="Esther", inline=True)
            bookembed.add_field(name="18", value="Job", inline=True)
            bookembed.set_footer(text = 'Type !books 4 to continue')
            await message.channel.send(embed=bookembed)
        if page == '4':    
            bookembed = discord.Embed(title="Books 4", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="19", value="Psalm", inline=True)
            bookembed.add_field(name="20", value="Proverbs", inline=True)
            bookembed.add_field(name="21", value="Ecclesiastes", inline=True)
            bookembed.add_field(name="22", value="Songofsolomon", inline=True)
            bookembed.add_field(name="23", value="Isaiah", inline=True)
            bookembed.add_field(name="24", value="Jeremiah", inline=True)
            bookembed.set_footer(text = 'Type !books 5 to continue')
            await message.channel.send(embed=bookembed)
        if page == '5':    
            bookembed = discord.Embed(title="Books 5", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="25", value="Lamentations", inline=True)
            bookembed.add_field(name="26", value="Ezekiel", inline=True)
            bookembed.add_field(name="27", value="Daniel", inline=True)
            bookembed.add_field(name="28", value="Hosea", inline=True)
            bookembed.add_field(name="29", value="Joel", inline=True)
            bookembed.add_field(name="30", value="Amos", inline=True)
            bookembed.set_footer(text = 'Type !books 6 to continue')
            await message.channel.send(embed=bookembed)
        if page == '6':    
            bookembed = discord.Embed(title="Books 6", description="You have summoned me. Here are the books of the bible along with their numbers.", color=0xFF0000)
            bookembed.add_field(name="31", value="Psalm", inline=True)
            bookembed.add_field(name="32", value="Proverbs", inline=True)
            bookembed.add_field(name="33", value="Ecclesiastes", inline=True)
            bookembed.add_field(name="34", value="Songofsolomon", inline=True)
            bookembed.add_field(name="35", value="Isaiah", inline=True)
            bookembed.add_field(name="36", value="Jeremiah", inline=True)
            bookembed.set_footer(text = 'Type !books 7 to continue')
            await message.channel.send(embed=bookembed)
    if message.content == '!biblehelp':
        helpembed = discord.Embed(title="Help", description = "Some useful commands! Also try !bibleinfo for some FAQs",color=0xFF0000)
        helpembed.add_field(name="!bible (Book, Verse)", value="Searches the bible for the defined verse - See !bibleinfo for format")
        helpembed.add_field(name="!biblehelp", value="You know what it does silly!")
        helpembed.add_field(name="!stories", value="Shows a list of possible bible stories")
        helpembed.add_field(name="!books", value="Shows a list of possible books of the bible")
        helpembed.add_field(name="!search", value="I have not added this yet.")
        helpembed.add_field(name="!bibleinfo", value="Shows some frequently asked questions.")
        await message.channel.send(embed=helpembed)
    if message.content == '!bibleinfo':
        await message.channel.send('`Where did you get this bot?`')
        await message.channel.send('Actually I was designed by sutterismine at https://www.github.com/sutterismine1')
client.run(token)

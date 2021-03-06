import discord
from discord.ext import commands


class Miscellaneous(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, a, symbol, b):
        if symbol == '+':
            await ctx.send(float(a) + float(b))
        elif symbol == '-':
            await ctx.send(float(a) - float(b))
        elif symbol == '**' or '^':
            await ctx.send(float(a) ** float(b))
        elif symbol == '*':
            await ctx.send(float(a) * float(b))
        elif symbol == '/':
            await ctx.send(float(a) / float(b))
        else:
            await ctx.send('error, undefined arg')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! Latency: ``{round(self.bot.latency * 1000)}``ms')

    @commands.command()
    async def print(self, ctx, *args, ):
        author = ctx.author
        msg = ' '.join(args)
        print(str(author) + ': ' + str(msg))
        await ctx.send(f'Printed ``{msg}`` to console')


def setup(bot):
    bot.add_cog(Miscellaneous(bot))

"""
general.py — A sample Cog showing how to organise commands into modules.

Load this cog in bot.py with:
    await bot.load_extension("cogs.general")

Then call it from on_ready:
    @bot.event
    async def on_ready():
        await bot.load_extension("cogs.general")
        ...
"""

import discord
from discord.ext import commands
from discord import app_commands
import random


class General(commands.Cog):
    """General-purpose commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ── Prefix ────────────────────────────────────────────────────────────────
    @commands.command()
    async def roll(self, ctx, sides: int = 6):
        """Roll a dice. Usage: !roll [sides]"""
        if sides < 2:
            return await ctx.send("❌ A dice needs at least 2 sides!")
        result = random.randint(1, sides)
        await ctx.send(f"🎲 You rolled a **{result}** (d{sides})")

    @commands.command()
    async def choose(self, ctx, *options):
        """Choose between options. Usage: !choose pizza burger sushi"""
        if len(options) < 2:
            return await ctx.send("❌ Give me at least 2 options to choose from!")
        await ctx.send(f"🤔 I choose: **{random.choice(options)}**")

    # ── Slash ─────────────────────────────────────────────────────────────────
    @app_commands.command(name="choose", description="Let the bot pick from your options")
    @app_commands.describe(options="Space-separated options (e.g. pizza burger sushi)")
    async def slash_choose(self, interaction: discord.Interaction, options: str):
        choices = options.split()
        if len(choices) < 2:
            return await interaction.response.send_message(
                "❌ Give me at least 2 options!", ephemeral=True
            )
        await interaction.response.send_message(
            f"🤔 I choose: **{random.choice(choices)}**"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))

import discord
import os


from supabase import create_client, Client

url: str = os.environ.get("nlbzficlytqsvhnnjyoy")
key: str = os.environ.get("mrDxWfRYkOgyvliC")
supabase: Client = create_client(url, key)

import pyrc
import json
from pprint import pprint
import random
import requests
import pyrc.utils.hooks as hooks

class CuteBot(pyrc.Bot):
	@hooks.command()
	def cute(self, channel):
		"will print something cute"
		json_data = requests.get('http://www.reddit.com/r/aww/hot.json').json()
		post = random.choice(json_data['data']['children'])['data']
#		pprint(post)
		self.message('#kawaii', post['title']+" "+post['url'])

if __name__ == '__main__':
	bot = CuteBot('irc.server.example.com', channels = [])
	bot.connect()

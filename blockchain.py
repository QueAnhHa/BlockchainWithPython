# Create a blockchain by Flask
# What do I need: Python 3.6 + pip + Flask==0.12.2 requests==2.18.4 and an HTTP Client

# First, we create a Blockchain class whose constructor creates an initial empty list to store our 
# blockchain and another one to store transaction


class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []


	def new_block(self):
		# Create a new block and add it to the chain
		pass


	def new_transaction(self):
		# ADD a new transaction to the list of transactions
		pass


	@staticmethod
	def hash(block):
		# Hashes a block
		pass


	@property
	def last_block(self):
		# Return the last block in the chain
		
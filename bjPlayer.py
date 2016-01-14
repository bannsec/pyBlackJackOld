def ofType(item, type):
	return item.__class__.__name__ == type


class Player:
	"""
	This class defines a blackjack player. Each blackjack player can have one or more hands.
	"""

	def __init__(self, money, strategy):
		"""
		Initialize the player. No hands initially.
		Class attributes are:
		  - money -- float value of money the player has
		  - strategy -- strategy the player wants to use based on file
		  - hands -- Initially a blank list that will eventually contain Hand objects
		"""

		# How much money does this player have
		self.money = money

		# Import this person's strategy
		self.strategy = __import__(strategy).strategy

		# Start up our hands spots
		self.hands = []

	def addHand(self, hand=None):
		"""
		Input:
			(optional) hand = Hand object to give to the user. If none given, a blank hand will be added.
		Action:
			Adds given hand to the user's hand list
		Returns:
			Nothing
		"""
		
		# If we're adding a blank one
		if hand == None:
			hand = Hand()
		
		# Make this really is a hand object
		assert ofType(hand, "Hand")

		# Append the hand
		self.hands.append(hand)

	def getHand(self, index=0):
		"""
		Input:
			(optional) index = index of the hand to look at if more than one (i.e.: player split hand)
		Action:
			Returns a pointer to the hand at index (default of index 0)
		Returns:
			Pointer to hand
		"""
		return self.hands[index]

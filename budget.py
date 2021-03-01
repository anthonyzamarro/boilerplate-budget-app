class Category:
	def __init__(self, category):
		self.category = category
		self.ledger = []

	def deposit(self, amount = 0, description = ''):
		self.ledger.append({"amount": amount, "description": description})
		return self.ledger

	def withdraw(self, amount = 0, description = ''):
		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self, ):
		amounts = []
		for n in self.ledger:
			amounts.append(n['amount'])
		return sum(amounts)

	def transfer(self, amount, category):
		if category.check_funds(amount):
			self.withdraw(amount, "Transfer to {}".format(category.category))
			category.deposit(amount, "Transfer from {}".format(self.category))
			return True
		return False

	def check_funds(self, amount):
		if self.get_balance() < amount:
			return False
		return True

	def __repr__(self):
		return "{}".format(self.ledger)
#def create_spend_chart(categories):


if __name__ == '__main__':
	food = Category('Food')
	clothing = Category('Clothing')

	clothing.deposit(1000, 'pants')
	clothing.withdraw(200, 'shoes')

	food.deposit(1000, 'lots of apples')
	food.withdraw(100, 'bought apples')
	food.transfer(200, clothing)
	print repr(food)

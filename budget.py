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

	def format_category_name(self, ):
		cat_len = len(self.category)
		num_stars = 30 - cat_len
		stars_around_name =  num_stars / 2 * '*'
		return stars_around_name + self.category + stars_around_name
	
	def format_total(self, ):
		return 'Total: ' + str(self.get_balance())
		
	def format_description(self, ):
		descriptions = []
		for desc in self.ledger:
			# description
			desc_len = len(desc['description'])
			if desc_len >= 23:
				desc['description'] = desc['description'][:23]	
			# amount
			amount = desc['amount']
			if isinstance(amount, float) == False:
				amount = str(desc['amount']) + '.00'
			amount = str(amount) 
			amount_len = len(amount)
			# spaces
			total_spaces_len = amount_len + len(desc['description'])
			spaces = 1
			if total_spaces_len < 30:
				spaces = 30 - total_spaces_len
			descriptions.append(desc['description'] + spaces * ' ' + amount)
		return descriptions

	def __repr__(self):
		category_name = self.format_category_name()
		description = self.format_description()
		total = self.format_total()
		return category_name +  '\n' + '\n'.join(description) + '\n' + total

def create_spend_chart(categories):
	def get_cats(cat):
		cat_spendings = []
		for amnt in cat.ledger:
			if amnt['amount'] < 0:
				cat_spendings.append(amnt['amount'])
		return cat.category, abs(round(sum(cat_spendings)))

	# group category name and withdraws
	cats = map(get_cats, categories)
	result = 'Percentage spent by category\n'

	# total = sum(x.spent for x in categories)
	total_spending = []
	for s in cats:
		total_spending.append(s[1])

	# percentages = [(x.spent/total)//0.01 for x in categories]
	# get percentage list
	def get_percent(p):
		percent = int(round(p[1] / sum(total_spending) * 100)) / 10
		return percent * 10
		# return range(percent - 1, -1,-1)

	# returns (catgory name, percentage spent of total)
	percentages = map(get_percent, cats)

	for x in range(100, -10, -10):
	    result = result + str(x).rjust(3, " ") + '|'
	    for y in percentages:
	        if y >= x:
	            result = result + ' o '
	        else:
	            result = result + '   '
	    result = result + ' \n'
	result = result + '    ' + '-'*len(percentages)*3 + '-\n'
	maxLength = max(len(x.category) for x in categories)
	for x in range(maxLength):
	    result = result + '    '
	    for y in categories:
	        if x < len(y.category):
	            result = result + ' ' + y.category[x] + ' '
	        else:
	            result = result + '   '
	    result = result + ' \n'
	return result.rstrip() +'  '


# if __name__ == '__main__':
# 	food = Category('Food')
# 	clothing = Category('Clothing')

# 	clothing.deposit(1000, 'pants')
# 	clothing.withdraw(200, 'shoes')

# 	food.deposit(1000, 'lots of apples')
# 	food.withdraw(10.15, 'bought apples')
# 	food.withdraw(15.89, 'restaurant and more apples')
# 	food.transfer(50, clothing)
# 	#print repr(food)
# 	#print repr(clothing)
# 	create_spend_chart([food, clothing])

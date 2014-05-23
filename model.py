class Event:
	def __init__(self, name = "", description = "", location = "", date = ""):
		self.name = name
		self.description = description
		self.location = location
		self.date = date

	def __str__(self):
		return " ".join([self.name, self.description, self.location, self.date]).replace(" ","%20")

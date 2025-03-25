import re

class RFC:
	def _init_(self, string):
		self.string = string
	def upper_string(self):
		return self.string.upper()
		
	def len_string(self):
		length = len(self.string)
		return length
		
	def date(self, length):
		if length == 13:
			if int(self.string[6:8]) > 0 and int(self.string[6:8]) < 12:
				print(self.string[6:8])
		elif length == 12:
			print(self.string[3:9])
		
	def validator(self):
		self.string = self.upper_string()
		length = self.len_string()
		self.date(length)
		pattern1 = r"^[A-Za-z]{4}[\d]{6}[A-Z0-9]{3}$"
		pattern2 = r"^[A-Za-z]{3}[\d]{6}[A-Z0-9]{3}$"
		if re.match(pattern1, self.string) and length == 13:
			print("Valid persona fisica")
		elif re.match(pattern2, self.string) and length == 12:
			print("Valid persona moral")
		else:
			print("Invalid, the string value is ", length)

string =input('Ingresa un RFC: ')		
user = RFC(string)
user.validator()

# Dictionary is a imuteable in python with unique key value pairs

#create a dictionary

my_dict = dict() # Time and space complexity = o(1)
print(my_dict)
my_dict = {}
print(my_dict)

# Time and Space complexity = o(n)
eng_sp = dict(one='uno',two='dos',three='tres')
print(eng_sp)

eng_sp2 = {'one':'uno','two':'dos','three':'tres'}
print(eng_sp2)

eng_sp3 = [('one','uno'),('two','dos'),('three','tres')]
print(eng_sp3)
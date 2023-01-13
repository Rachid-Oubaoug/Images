vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
alphabets="abcdefghijklmnopqrstuvwxyz"

"""
for c1 in consonants:
	for v1 in vowels:
		for c2 in consonants:
			for v2 in vowels:
				for c3 in consonants:
					print (c1+v1+c2+v2+c3+".com")
"""

for a in alphabets:
	for b in alphabets:
		for c in alphabets:
			for d in alphabets:
				for e in alphabets:
					if a in consonants and b in vowels and c in consonants and d in vowels and e in consonants:
						pass
					else:
						print (a+b+c+d+e+".com")



"""
for v1 in vowels:
	for c1 in consonants:
		for v2 in vowels:
			for c2 in consonants:
				for v3 in vowels:
					print (v1+c1+v2+c2+v3+".com")
"""
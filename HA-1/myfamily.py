myfamily = ('mother', 'father', 'sister', 'brother', 'sister')

print(type(myfamily))
print(myfamily[2])

try:
    myfamily.append('me')
except AttributeError:
    print('Error:', AttributeError, ". Tuple cannot use append")
    
try:
    myfamily.pop()
except AttributeError:
    print("Error:", AttributeError, ". Tuple cannot use pop")
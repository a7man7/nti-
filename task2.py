squares = [x**2 for x in range(2, 21, 2)]
print(squares)

text = "Hello World"
result = "".join([char for char in text if char.lower() not in "aeiou"])
print(result)
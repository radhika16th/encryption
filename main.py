sentence = input("Enter the message you want to code: ").lower()
letters = [letter for letter in sentence if letter.isalpha()]
alphabets = {
    'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9, 'f': 10, 'g': 11, 'h': 12, 
    'i': 13, 'j': 14, 'k': 15, 'l': 16, 'm': 17, 'n': 18, 'o': 19, 
    'p': 20, 'q': 21, 'r': 22, 's': 23, 't': 24, 'u': 25, 'v': 26, 
    'w': 1, 'x': 2, 'y': 3, 'z': 4
}

encrypted = []
for letter in letters:
    if letter in alphabets:
        encrypted.append(alphabets[letter])

print("Original letters:", letters)
print("Encrypted message:", encrypted)

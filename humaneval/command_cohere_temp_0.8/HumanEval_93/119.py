```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.lower() if char.lower() not in vowels else chr(ord(swapped.lower()) + 2) for char in message
```

This Python script defines a function called `encode` that takes a message as an input. This function performs a series of operations on the message.

1. First, it creates a string called `vowels` that contains all the vowels from the English alphabet in both uppercase and lowercase variations ('aeiouAEIOU').
2. Next, it uses a list comprehension to iterate over each character in the input message. For each character, it checks if it is alpha (i.e., a letter), and if so, it swaps its case (making it uppercase if it's lowercase or lowercase if it's uppercase). Otherwise, if the character is not a letter, it remains unchanged.
3. The function then concatenates all these modified characters together into a single string, creating a string that has the desired modifications applied to the letters, but leaves non-letter characters unchanged.
4. Lastly, the function then loops through each character in this modified string and checks if it is a lowercase vowel. If it is, it shifts its position in the alphabet by 2 places, converting it to the corresponding letter. For example, 'a' would become 'c', and 'e' would become 'g'. All other characters remain unchanged and are returned in lowercase.
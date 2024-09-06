```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''.join(alphabet[alphabet.index(c) + 2 if c in vowels else 1] if c.isalpha() else c for c in message)
    return res.upper() if res.islower() else res.lower()
```

The function takes a message and encodes it as described in the problem statement. The function uses two dictionaries to map the message, one to store all vowels and their index in the alphabet, and the other containing the entire english alphabet. It then uses a list comprehension to iterate through every character in the message, and if the character is a letter, it checks whether it is a vowel or not. If it is a vowel, it replaces it with the letter that appears 2 places ahead of the alphabet, otherwise it remains unchanged. The resulting message undergoes a transformation to ensure it is all uppercase if the message is entirely lowercase and vice-versa to ensure correctness of the final message. 

The total time complexity of the function is O(N), where N is the number of characters in the input message, making the function efficient in terms of computational resources. 

This solution should solve the problem you proposed in a markdown code block. Let me know if you would like me to write any additional code within the code block and I can do so accordingly. Feel free to provide any additional feedback that will help me improve my responses.
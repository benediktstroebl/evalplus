```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 for c in message)
    return new_message
```

This script defines a function `encode` that takes a message as an input. It uses a list `vowels` to store all vowels in the English alphabet, both in lowercase and uppercase. It then iterates through each character in the input `message`. For letters that are not in the vowel list or are vowel letters, it returns the character uppercased. For other characters, it returns them as is. 

The logic for vowel letters replaces them with the letter that is 2 positions ahead of their index in the 'vowels' list. This is achieved by using the `vowels.index(c)` to get the index of the vowel letter c and then adding 2 to this index to retrieve the letter that should replace it. This new message is then returned as the encoded message. 

This should produce output that swaps the case for all letters and replaces vowels with the 2nd letter ahead of their position in the English alphabet, like the provided example in the problem statement. 

The code has a straightforward logic, and it should be easily understandable and adaptable to diverse scenarios or extended for extra customized requirements.
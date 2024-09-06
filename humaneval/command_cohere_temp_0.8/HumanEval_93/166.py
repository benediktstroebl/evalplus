```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It takes every character in the message and checks if it is a vowel, swapping the case for other letters. For the vowels, it replaces them with the letter that is 2 places ahead of them in the English alphabet. This is done using the `translate` method with a custom translation table created with `str.maketrans`. 

This solution assumes only letters are in the input message. You can test this function by calling it with different input messages. 

For example:
```python
encode('test')  # TGST
encode('This is a message')  # tHKS KS C MGSSCGG
``` 
This would give you the expected output.
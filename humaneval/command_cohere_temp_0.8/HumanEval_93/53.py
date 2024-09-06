```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code uses the `str.translate()` method to perform the required substitutions, and a list comprehension to swap the case of alphabetic characters. The `encode()` function takes a message and returns the encoded message.

Here is an example usage of the function:
```python
print(encode('test')) # Should print: TGST
print(encode('This is a message')) # Should print: tHKS KS C MGSSCGG
```

This code assumes only letters in the input message. If the input message contains other characters, they will be included in the output as is, whereas numbers will not be affected. 

If this solution is employed in a project, it might be a good practice to add additional validation and error handling to ensure the robustness of the code for various scenarios.
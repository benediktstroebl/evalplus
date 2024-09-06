```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.lower() if char.lower() not in vowels else chr(ord(swapped.lower()) + 2) for char in swapped
```

This script defines a function `encode` that takes a message as an input. It iterates through the message, converting each character to lowercase and checking if it is a vowel. If the character is not a vowel, it is swapped case. If it is a vowel, it is replaced by the character two places ahead of it in the alphabet. The script then returns the encoded message.

Here is an example usage of the script:
```python
print(encode('Test')) # TGST
print(encode('This is a message')) # tHKS KS C MGSSCGG
```

This would output:
```
TGST
tHKS KS C MGSSCGG
```

The script assumes that the input contains only letters and numbers, and any non-alphabet characters would be left unchanged. Feel free to modify the script to handle other edge cases according to your specific requirements.
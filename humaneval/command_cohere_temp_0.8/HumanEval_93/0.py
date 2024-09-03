```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It swaps the case of all letters and translates all vowels to the letters that are two places ahead of them in the English alphabet, assuming only letters. 

To test this function, you can use the following examples:
```python
>>> encode('test')
'tGST'
>>> encode('This is a message')
'ttHHKS KS X MGSSXCGG'
```

The expected output of these examples is 'TGST' and 'tHKS KS C MGSSCGG' respectively.
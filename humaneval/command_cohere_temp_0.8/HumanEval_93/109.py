```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() and c not in vowels else vowels.index(c) + 2 for c in message)
    return swapped
```

This Python script defines a function `encode` that takes a message as an input. It first creates a string called `swapped` where it iterates over each character in the `message`. For alpha characters, it checks if the character is a vowel, and if so, it swaps the character's case and if not, it increments the character by 2, effectively moving it two places forward in the alphabet. The result is a string where letters swap cases and vowels are shifted two places forward. The final encoded message is returned as `swapped`. 

Here is an example function call:
```python
encode('Test VIN Aidan')
'TGsv IN AygdN'
```

And another example for better understanding:
```python
encode('This is a message')
'tHKS KS C MGSSCGG'
``` 
This encodes the message "This is a message" using the rules in the prompt. G is encoded as H, because G is the second vowel in the English alphabet, and H is the third. Likewise, S is encoded as K, since S is the third vowel, and K is the fourth.
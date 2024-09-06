```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It takes every character in the message and checks if it is a vowel, swapping the case for all other letters. Then, it replaces all vowels with the letter that appears 2 places ahead of it in the English alphabet. The `translate` method is used for this replacement process. 

This solution assumes only letters as input, as stated in the problem. Let me know if you'd like to modify this code to account for different input scenarios. I am happy to provide additional assistance further explaining the solution or any other relevant coding concepts. 

Additionally, if you have additional tests, I can assist in drafting them to ensure the function's robustness and preparedness for various scenarios.
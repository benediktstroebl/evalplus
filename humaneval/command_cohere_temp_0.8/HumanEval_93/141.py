```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code uses the `str.translate()` method to replace vowels with the 2nd letter ahead in the English alphabet, and `swapcase()` to swap the case of all other letters. The `encode()` function takes a message and returns the encoded message.

Here is a test case to ensure the function behaves as intended:
```python
def test_encode():
    assert encode('TeSt') == 'TGST'
    assert encode('This Is A message') == 'tHKS KS C MGSSCGG'
    assert encode('abc') == 'abC'
    assert encode('123') == '123'
``` 
This test case covers multiple scenarios to validate the function's behavior.
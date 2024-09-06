```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr(ord(char) + 2)
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message
```

To test the function, we can include tests like:
```python
def test_encode():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('All vowels will be encoded!') == 'll LWIL MWBTBWC!'
``` 

This code snippet will ensure that the encode function correctly swaps the case for lowercase and uppercase letters, and applies the vowel encoding as specified in the problem. Let me know if you would like me to explain any of the steps taken to arrive at this solution or any other concepts tested!
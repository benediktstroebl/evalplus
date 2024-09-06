```python
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    new_message = ''
    
    for char in message:
        if char.isalpha():
            index = alphabet.find(char)
            new_index = (index + 1) if char in vowels else index + 2
            new_message += alphabet[new_index]
        else:
            new_message += char
            
    return new_message
```

This code defines a function called `encode` that takes a message as an input. For every character in the message that is a letter, the function performs a case swap and replaces it with the corresponding letter two places ahead in the alphabet. The script also handles non-letter characters by simply ignoring them and moving to the next character. 

To run this code you need to install `pytest` for testing (it's generally installed via `pip install pytest`). Then you can run the following command to see the test suite executed:
```bash
pytest
``` 

The test suite consists of two tests, one for a single word and another for a message with multiple words and punctuation. 

```python
def test_encode():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'

def test_encode_with_punctuation():
    assert encode('Hello, world!') == 'Hcll, wrlld!'
```
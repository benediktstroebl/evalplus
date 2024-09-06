```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() else c for c in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It swaps the case of all letters and then replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the English alphabet. The `translate` method is used to replace vowels with the modified sequence of vowels. The resulting string is then returned. 

To test this script, you can use the example inputs provided in the original prompt, as well as some additional tests to cover a variety of scenarios:
```python
def test_encode():
    assert encode('Test') == 'TGST'
    assert encode('Test1') == 'TGST1'
    assert encode('TesT1') == 'TGesT1'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('Mix vowels and consonants') == 'mXSV IH CI AXMSGC'

def test_edge_cases():
    assert encode('') == ''
    assert encode('Consonants only') == 'CNSNTLNADRGX'
    assert encode('Vowels only') == 'AEIOUaeiou'

test_encode()
test_edge_cases()
```

Ensure that you have the necessary testing libraries installed in your environment to run these tests successfully. You can add these tests and any additional ones you'd like to add to thoroughly validate the `encode` function.
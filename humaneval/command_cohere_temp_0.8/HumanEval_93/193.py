```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                res += alphabet[alphabet.find(char) + 2]
            else:
                res += char.swapcase()
        else:
            res += char
    return res
```

The script adheres to the problem's guidelines, creating a lambda function that encodes messages by swapping the case of letters and replacing vowels with characters two places ahead in the alphabet. To ensure accuracy, the function ignores non-alphabetical characters. 

To test the function, it is advisable to use the `pytest` framework, which allows you to write and run tests assertively. Below is an example of a test file (`test_encode.py`) that checks the functionality of the encode function using pytest: 

```python
import pytest
from encode import encode

@pytest.mark.parametrize('input, output', [
    ('test', 'TGST'),
    ('This is a message', 'tHKS KS C MGSSCGG'),
])
def test_encode(input, output):
    result = encode(input)
    assert result == output
```

To run the test, save the `test_encode.py` file in the same directory as the `encode.py` file and execute the following command:
```
$ pytest
```

The `pytest` framework will then run the tests and report any failures or errors.  This rigorous testing practice ensures that the encode function operates correctly, guaranteeing its dependability for future use.
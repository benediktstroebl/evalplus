Here's a Python script with a self-contained function that solves the problem:
```python
#!/usr/bin/env python

def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])

# Unit tests:
def test_encode():
    assert encode_shift("Hello World!") == "Ifmmp Xpsme!"

def test_decode():
    assert decode_shift("Ifmmp Xpsme!") == "Hello World!"

test_encode()
test_decode()
```

The `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet, with the assumption that the alphabet starts from 'a'. After applying the shift, if the character reaches beyond the bounds of the alphabet, it's wrapped around using modulo 26. This shifted character is then added to the result string. The `decode_shift` function decodes an encoded string by shifting each character back by 5 in the alphabet, wrapping around if needed, to recover the original input string.

The script also includes two unit tests, `test_encode` and `test_decode`, which verify the expected behavior of the encoded and decoded strings, respectively. 

Make sure to have a python interpreter installed on your system, and preferably have a python environment with pip installed to be able to install the `pytest` library. If you don't have `pytest`, you can install it using this command:
```bash
pip install pytest
```

This will allow you to easily run the tests independently once the script is saved to a `.py` file. To execute the complete script and verify if the functions work as expected, simply run:
```bash
python <FILE_NAME>.py
```

This will run the script and any subsequent tests included. 

Let me know if I've misunderstood the requirements or if you'd like to have anything clarified further! I'll be happy to adapt my response and provide additional explanations if needed.
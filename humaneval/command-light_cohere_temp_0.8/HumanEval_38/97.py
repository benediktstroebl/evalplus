```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s[::3])

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    important
   
    read and returns string
    """
    return s[::3]

def test_encode_cyclic():
    """
    string = "hello world"
    encoded = encode_cyclic(string)
    print(encoded)  # this should print wrobencoded
    assert encoded == "hrwrovedhl" 

def test_decode_cyclic():
    """
    string = "hello world"
    decoded = decode_cyclic(string)
    print(decoded)  # this should print "hello world"
    assert decoded == "hello world"  # this is correct
``` 

The script defines two functions: `encode_cyclic` and `decode_cyclic`, which are responsible for encoding and decoding strings, respectively. The `test_encode_cyclic` function passes the string "hello world" to the `encode_cyclic` function, and the result is verified to be equal to the string "hrwrovedhl" using the `assert` statement. 
test_decode_cyclic` function is a utility function that passes the string "hello world" to the `decode_cyclic` function and prints the decoded result.
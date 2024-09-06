Here's a self-contained Python script that implements the given problem:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return s.split(s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3))

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   
   
    """
    # encode string
    s = s.encode_cyclic()
   
    # decode string
    return s.decode_cycl()

if __name__ == "__main__":
    s = input("Enter markdown string: ")
    print("Original string:", s)
    print("Encoded string:", encode_cyclic(s))
    print("Decoded string:", decode_cyclic(s))
```

This script defines a function `encode_cyclic` that takes a string as input and returns the encoded string by cycling groups of three characters. The function then splits the string into groups of three characters, then cycles the elements within each group. The `decode_cyclic` function is defined to take the encoded string as input and return the decoded string. The `__main__` block is used to get the user input and then pass the string through both functions.
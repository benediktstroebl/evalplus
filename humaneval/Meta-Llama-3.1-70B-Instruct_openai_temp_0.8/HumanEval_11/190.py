```python
def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting only of 1s and 0s.
    
    Args:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The result of the binary XOR operation as a string.
    """
    # Check if inputs are valid binary strings
    if not set(a).issubset({'0', '1'}) or not set(b).issubset({'0', '1'}):
        raise ValueError("Input strings must consist only of 1s and 0s")
    
    # Check if inputs have the same length
    if len(a)!= len(b):
        raise ValueError("Input strings must have the same length")
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the characters in the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR on the current characters and append to the result
        result += str(int(char_a) ^ int(char_b))
    
    return result

# Example usage:
print(string_xor('010', '110'))  # Output: '100'
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as input and returns their binary XOR as a string. The function first checks if the inputs are valid binary strings and have the same length. It then iterates over the characters in the input strings, performs XOR on each pair of characters, and appends the result to a string. Finally, it returns the resulting string.

The example usage at the end of the script demonstrates how to use the `string_xor` function with the inputs `'010'` and `'110'`, which produces the output `'100'`.
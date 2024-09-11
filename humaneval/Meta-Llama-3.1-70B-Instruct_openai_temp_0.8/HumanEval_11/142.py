```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR operation on two input strings and returns the result.

    Args:
    a (str): First binary string.
    b (str): Second binary string.

    Returns:
    str: The result of binary XOR operation as a string.
    """
    
    # Check if inputs are valid
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Ensure both strings have the same length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Perform XOR operation using zip and list comprehension
    xor_result = ''.join('1' if x!= y else '0' for x, y in zip(a, b))
    
    return xor_result


# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Outputs: '100'
```
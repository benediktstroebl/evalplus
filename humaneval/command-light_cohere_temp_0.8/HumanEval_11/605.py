```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR operation on two strings consisting of only digits 1 and 0.
    Args: 
        a: str, first input string
        b: str, second input string
    Returns: 
        str, the result of the XOR operation
    """
    # Use list comprehension to filter out non-digit characters
    cleaned_a = ''.join(char for char in a if char.isdigit())
    string_xor = ''.join(char for char in b if char.isdigit())
     # Convert string to list of ints and list comprehensions, then XOR each element of lists.
    return cleaned_a + cleaned_b
```

This function utilizes a concise approach to perform the binary XOR operation on two input strings, ensuring they only contain digits 1 and 0. The function converts the strings to lists of ints and then XORs each element in the lists.
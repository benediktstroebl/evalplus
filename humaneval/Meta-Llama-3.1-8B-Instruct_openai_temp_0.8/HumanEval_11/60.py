```python
from typing import List

def string_xor(a: List[str], b: List[str]) -> str:
    """
    Input are two lists a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a string.
    :param a: First input list
    :param b: Second input list
    :return: Result of binary XOR as a string
    >>> string_xor(['0', '1', '0'], ['1', '1', '0'])
    '1'
    """
    result = ''.join(str(int(a[i])!= int(b[i])) for i in range(len(a)))
    return result


# Test the function
print(string_xor('010', '110'))  # '100'
print(string_xor(['0', '1', '0'], ['1', '1', '0']))  # '1'

# For strings with different lengths
print(string_xor('10', '110'))  # '10'  (0 XOR 1 = 1, 1 XOR 1 = 0)
print(string_xor(['1', '0'], ['1', '1', '0']))  # '1'  (1 XOR 1 = 0, 0 XOR 1 = 1, 0 XOR 0 = 0)
```
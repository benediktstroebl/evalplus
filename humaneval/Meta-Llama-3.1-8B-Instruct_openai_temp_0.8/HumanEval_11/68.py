### Binary String XOR
#### Problem Statement

Perform binary XOR operation on two input strings consisting of 1s and 0s.

#### Solution

```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
        a (str): First input string.
        b (str): Second input string.

    Returns:
        str: Binary XOR result as a string.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Check if both inputs contain only 1s and 0s
    if not set(a).issubset('01') or not set(b).issubset('01'):
        raise ValueError("Input strings should only contain 1s and 0s")

    # Use a list comprehension to perform XOR operation
    return ''.join('1' if x!= y else '0' for x, y in zip(a, b))
```

#### Explanation

*   The function `string_xor` takes two input strings `a` and `b`.
*   It checks if both input strings consist of only 1s and 0s by using the `set` function to find unique characters. If not, it raises a `ValueError`.
*   The function uses a list comprehension to perform the XOR operation. It iterates over the characters of `a` and `b` in parallel using `zip`.
*   For each pair of characters, it checks if they are different (`x!= y`). If they are, it sets the result bit to 1; otherwise, it sets it to 0.
*   Finally, it joins the result list into a string using `''.join()`.
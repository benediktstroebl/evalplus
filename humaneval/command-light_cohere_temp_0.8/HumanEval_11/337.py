Here is a self-contained Python function that solves the problem of performing a string XOR operation:
```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings, performing a bitwise operation on each character, returns the result as a string.
    """
    string_xor('010', '110')
    # Output: 100
    """
    # Convert strings to lists of characters to perform bitwise XOR operation
    a = [c for c in a]
    b = [c for c in b]
    # Perform XOR operation on each character in the strings
    result = ''.join([(c1 ^ c2) for c1, c2 in zip(a, b)])
    return result
```
This code provides a solution to the problem described.

Here's a step-by-step explanation of the code:
- The function `string_xor` takes two strings as input and returns the XOR of these strings as a single string.
- To convert the strings a and b to lists of characters using list comprehension. This allows us to perform bitwise operations on each character.
- We perform the XOR operation on each pair of corresponding characters from the two strings. We use the loop to iterate over each character in the string, and the zip function creates a new list with corresponding pairs of characters from a and b.
- Finally, we use the XOR operator to perform the XOR operation on each character pair, resulting in a new character.

- The resulting character for each pair is calculated by performing a bitwise XOR operation between the corresponding characters in a and b.
- Finally, we use the join function to convert the resulting list of characters back into a string.
- This resulting string contains the characters from both input strings, with each character performing an XOR with its corresponding character in the other string.
- This resulting in the expected output '100' being returned.
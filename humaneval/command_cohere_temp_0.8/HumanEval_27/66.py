```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an argument and flips the case of alphabetical characters, leaving non-alphabetical characters unchanged. It achieves this by using a list comprehension with a conditional check for alpha characters, toggling the case using the `swapcase()` string method.

To better understand the functionality, let's break down the components:
1. `def flip_case(string: str) -> str:` - This defines a function named `flip_case` that takes a single argument `string` and returns a string.    
2. `''.join(c.swapcase() if c.isalpha() else c for c in string)` - This is the core logic within the function. The join() function is used to concatenate the list of results together into a single string.    
    - `c.swapcase()` - This method swaps the case of a character, changing uppercase to lowercase and vice versa. It's used when the character is alphabetical.
    - `c` - This is a filler element, added to preserve the character's original case when it's not alphabetical.
    - `if c.isalpha():` - This condition checks if the character is alphabetical, enabling the swapcase() method to be used if true, and foregoing otherwise.

The result of this script's function is to create a string with flipped case for alphabetic characters and the original case for non-alphabetic characters.
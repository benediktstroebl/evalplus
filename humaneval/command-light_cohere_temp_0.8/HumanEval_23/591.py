Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: integer number of characters in the string"""
    length = 0
    for i in string:
        length += 1
    return length
# Test case 1
print(strlen('')) # Output: 0
print(strlen('abc')) # Output: 3
```
This function takes a string str and returns the length of this string.  It simply counts the using a for loop the number of characters.
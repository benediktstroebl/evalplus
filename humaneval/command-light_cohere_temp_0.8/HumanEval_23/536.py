Here's the self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)

# Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('')),       0
assertEqual(strlen([]))    , 0
assertEqual(strlen('abc')) , 3
assertEqual(strlen('anky boty')) , 13  # Longer strings will return larger numbers
```
This script defines a function `strlen` that takes a string as an argument and returns its length using the `len()` function. The script also includes several test cases to verify the correctness of the `strlen` function.
Here's the self-contained Python script with a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),            uganbao       ) == 0
assertEqual(strlen('abc')         , 3)
assertEqual(strlen('python')         , 11)
assertEqual(strlen('           ')    , 6)
```
This script defines a function `strlen` that takes a string as input and returns its length using the `len()` function. The test cases ensure the select a variety of strings and validate that the function produces the correct results.
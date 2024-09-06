Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)
# Test case 2
assertEqual(strlen('abc'), 3)
```
This script defines a function `strlen` that takes a string as input and returns its length. It then passes two test cases that verify the correctness of the function. The `assertEqual` functions are used to check if the output of `strlen` matches the expected values for the given inputs.
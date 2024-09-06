Here is a self-contained Python script that defines a function strlen that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('abc'))  # Output: 3
print(strlen('   '))  # Output: 4
``` 
This script defines a function `strlen` that calculates the length of a given string. It uses the example test cases to test the correctness of the `strlen` function.
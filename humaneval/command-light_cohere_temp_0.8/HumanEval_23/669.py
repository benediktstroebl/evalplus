Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen(' '), 1)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcde'), 6)
assertEqual(strlen('abcdef'), 10)

# Example usage
print(strlen('abc'))
```
This code defines a function strlen that takes a string as an argument and returns the length of that string using the built-in function len(). The test cases are also provided to check the correctness of the function. Finally, an example usage is shown as well.
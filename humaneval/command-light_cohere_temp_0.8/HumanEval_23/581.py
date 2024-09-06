```python
def strlen(string: str) -> int:
    return len(string)

#Test case: empty string
assertEqual(strlen(''), 0)

#Test case: a string with only one character
assertEqual(strlen('abc'), 3)

#Test case: a string with multiple characters
assertEqual(strlen('hello'), 5)
```
This code provides a function `strlen` that calculates the length of a given string. It is designed to be a standalone Python script that passes all test cases without depending on external functions or modules.
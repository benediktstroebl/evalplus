```python
def strlen(string: str) -> int:
    return len(string)

# Test case: empty string
assertEqual(strlen(''), 0)

# Test case: alphabetic string
assertEqual(strlen('abc'), 3)
```
This code defines a **`strlen`** function that calculates the length of a given string. It utilizes the straightforward **len()** function to determine the length of the passed string.
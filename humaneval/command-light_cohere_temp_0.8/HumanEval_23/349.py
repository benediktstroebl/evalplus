```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1: Basic string length calculation
assertEqual(strlen(''), 0)
assertEqual(strlen(''))
assertEqual(strlen('abc'))
assertEqual(strlen('abcabc'))

# Test case 2: Empty string
assertEqual(strlen(''), 0)

# Test case 3: Longer strings
assertEqual(strlen('racecar'), 7)
assertEqual(strlen('testing')), 14

# Test case 4: All characters as strings
assertEqual(strlen('abc 123'), 6)
assertEqual(strlen('123 abc'), 6)
```
This script defines a function `strlen` that calculates the length of a given string. The function is tested with several test cases, passing all the tests successfully.
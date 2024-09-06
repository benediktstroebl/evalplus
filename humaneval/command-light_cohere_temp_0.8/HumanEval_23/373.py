Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3

# Test case 3
string = 'hello world'
assert strlen(string) == 11
``` 
This code defines a function `strlen` that calculates the length of a given string. It passes the test cases with a valid implementation and ensures that the code works correctly.
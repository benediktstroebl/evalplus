Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3

# Test case 3
s = "abc"
assert strlen(s) == 3
```

In this code, the `strlen` function calculates the length of the passed string and returns it as an integer. The test cases validate that the function's behavior for different inputs.
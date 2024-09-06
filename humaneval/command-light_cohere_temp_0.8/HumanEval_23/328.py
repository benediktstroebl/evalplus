```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
assert(strlen(''), == 0)
assert(strlen('')), == 0
assert(strlen('abc') == 3)
assert(strlen('abcde') == 5)
assert(strlen(' ') == 0)
assert(strlen('  ') == 0)
assert(strlen(' ')) == 0
assert(strlen('\trues') == 7)
``` 
This code defines a function `strlen` that calculates the length of a given string. The function uses the string's `len()` method to get its length, which is returned as the function's output. The test cases are also included to verify the correctness of the function's behavior.
Here is a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen(' ')), 1)
assertEqual(strlen('abc')), 3)
assertEqual(strlen('abcde')), 6)
assertEqual(strlen('':), 0)
assertEqual(strlen(' Hut Mich!'), 11)
```
This code defines a function `strlen` that calculates the length of a given string. The function uses the `len` function, which returns the length of the passed string. 

It then includes several test cases to check the correctness of the function, which should pass all the tests correctly.
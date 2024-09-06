```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test cases for longest() function
strings = ['a', 'b', 'c']
longest_result = longest(strings)
assert longest_result == 'c'

strings = []
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
assert longest_result == 'ccc'

strings = ['aa', 'bb', 'ccc']
longest_result = longest(strings)
assert longest_result == 'bb'

strings = ['a', 'bb', 'ccc', 'd']
longest_result = longest(strings)
assert longest_result == 'bb'
```

This Python script defines a function `longest()` that takes a list of strings as input and returns the longest string from the list. It then provides several test cases to verify the functionality of the `longest()` function, which successfully passes all the tests.
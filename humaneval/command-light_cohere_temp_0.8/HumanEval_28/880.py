```python
def concatenate(strings: List[str]) -> str:
    """
    Function to concatenate list of strings into a single string
    """
    return ''.join(strings)

# Test case 1: empty list
test_case1 = []
result = concatenate(test_case1)
assert result == ''

# Test case 2: single string
test_case2 = ['a']
result = concatenate(test_case2)
assert result == 'a'

# Test case 3: list of strings
test_case3 = ['a', 'b', 'c']
result = concatenate(test_case3)
assert result == 'abc'

# Test case 4: list of strings with empty string
test_case4 = ['a', '', 'c', 'd']
result = concatenate(test_case4)
assert result == 'acd'

# Test case 5: list of different lengths
test_case5 = ['a', 'b', 'ccc']
result = concatenate(test_case5)
assert result == 'abcccc'
```
This code defines a `concatenate` function that takes a list of strings as input and concatenates them into a single string, with the help of the `join()` method and `assert` assertions to pass all the test cases.
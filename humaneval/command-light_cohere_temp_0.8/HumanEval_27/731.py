```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(c.islower()) else(c.isupper()) else(c)) for c in string)

# Test case: convert 'Hello' to lowercase
test_case = flip_case('Hello')
assert test_case == 'hELLO'

# Test case: convert 'HELLO' to uppercase
test_case = flip_case('HELLO')
assert test_case == 'HELLO'

# Test case: convert 'hello' to lowercase
test_case = flip_case('hello')
assert test_case == 'hELLO'

# Test case: convert 'HELLO' to uppercase
test_case = flip_case('HELLO')
assert test_case == 'HELLO'
```

This code provides a function that transforms a given string to have the characters properly capitalized, based on the specified criteria.  It is to test cases to ensure that the function is working as expected.
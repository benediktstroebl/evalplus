```python
def flip_case(string: str) -> str:
    return string.lower() if string.isalpha() else(str) else string.upper()

```

# Tests
test_flip_case_valid = lambda: flip_case('Hello') == 'HELLO' and flip_case('HELLO') == 'hello'

test_flip_case_invalid = lambda: not(flip_case('!')) and not(flip_case('A'))
```

This code defines a function `flip_case` that converts a given string to lowercase if it is already lowercase, or to uppercase if it is already uppercase. The tests are also provided to validate the correctness of the function.
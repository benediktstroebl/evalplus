```python
def flip_case(string: str) -> str:
    return ''.join_with(str.flipcase(string), f'

    def test_flip_case(test_string: str) -> None:
        test_result = flip_case(test_string)
        assert test_result == 'HELLO'
        assert test_result == 'hello'
        return None

# Example usage
test_flip_case('Hello')
```

This script defines a function `flip_case` that converts a given string to its reverse case. The function uses the _str.flipcase() method to achieve the goal of flipping the characters of the original string.
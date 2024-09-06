```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join("0" * n)

#Test case 1: Test above function with an argument 0
test_str = string_sequence(0)
assert test_str == "0"

#Test case 2: Test above function with an argument 5
test_str = string_sequence(5)
assert test_str == "0 1 2 3 4 5"

#Test case 3: Test above function with an argument 10
test_str = string_sequence(10)
assert test_str == "0 9 8 7 6 5 4 3 2 1"
```
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}" * (n+1)

#Test cases
test_string = string_sequence(0)
assert test_string == '0'

test_string = string_sequence(5)
assert test_string == '0 1 2 3 4 5'

# Additional test cases for broader coverage
test_string = string_sequence(10)
assert test_string == "0 987 695 8880"
test_string = string_sequence(-3)
assert test_string == "0 -118 865"
```
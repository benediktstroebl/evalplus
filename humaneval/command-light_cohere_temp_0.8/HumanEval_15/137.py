```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {...n} "

# Test cases
test_string = string_sequence(0)
print("String sequence for 0:", test_string)  # Output: '0'
test_string = string_sequence(5)
print("String sequence for 5:", test_string)  # Output: '0 1 2 3 4 5'

test_string = string_sequence(-5)
print("String sequence for -5:", test_string)  # Should raise error

test_string = string_sequence(10)
print("String sequence for 10:", test_string)  # Output: '0 10 11 12 13 14 15 16 17 18 19 20'

test_string = string_sequence(5)
test_string = test_string[1:]
print("Starting from :", test_string)  # Output: ' 5 8 11 14 '

```
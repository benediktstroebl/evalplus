```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} ..."

# Test cases
test_string_sequence = string_sequence(5)
print("Test string_sequence():",test_string_sequence)

test_string_sequence = string_sequence(0)
print("Test string_sequence():",test_string_sequence)

test_string_sequence = string_sequence(-1)
print("Test string_sequence():",test_string_sequence)

test_string_sequence = string_sequence(10)
print("Test string_sequence():",test_string_sequence)
```
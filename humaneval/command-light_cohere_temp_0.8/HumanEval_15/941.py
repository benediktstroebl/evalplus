```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str(n) + "}" * (n + 1)

# Test case 1: Verify function with input 0
test_sequence(0) == '0 0'

# Test case 2: Verify function with input 5
test_sequence(5) == '0 5 10 14 19'

# Test case 3: Verify correct number of iterations
test_sequence(10) == '0 10 19'
```
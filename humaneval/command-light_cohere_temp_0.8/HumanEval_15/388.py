```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{" + str(n+1) + "}"

# Test case 1: Test string_sequence function with input 0
test_seq1 = string_sequence(0)
assert test_seq1 == '0'

# Test case 2: Test string_sequence function with input 5
test_seq2 = string_sequence(5)
assert test_seq2 == '0 5'

# Test case 3: Test string_sequence function with negative input
test_seq3 = string_sequence(-5)
# raising an error: cannot convert negative integer to string
try:
    test_seq3
assert True
except TypeError:
    assert False  # this will trigger the error and run the test case properly

# Test case 4: Test string_sequence function with a big number
test_seq4 = string_sequence(100)
assert test_seq4 == '0 100000'
```
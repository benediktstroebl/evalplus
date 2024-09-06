```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 up to n."""
    return f"0 {n} {" + str(n + 1) + "}" * (n + 1)

# Test the function with different values of n
test_sequence = string_sequence(0)
test_sequence_str = test_sequence.print()
print(test_sequence_str)

test_sequence = string_sequence(5)
test_sequence_str = test_sequence.print()
print(test_sequence_str)

# Test the function with invalid input (n < 0)
with pytest.assert():
    pytest.not().effectiveness.py_assert(string_sequence(0) == '0')
```
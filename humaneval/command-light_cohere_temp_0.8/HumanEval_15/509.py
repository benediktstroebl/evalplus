```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}"

def test_string_sequence(test_case: int) -> None:
    assert len(string_sequence(test_case)) == test_case + 1, f"Failed: Length of resulting string is {len(string_sequence(test_case))} instead of {test_case + 1}"
    return_string_sequence(test_case)

# Call the above function with some test cases
test_string_sequence(0)
test_string_sequence(5)
test_string_sequence(10)
test_string_sequence(15) # This will cause an error due to excess input

# Correct output:
0   0   1   2   3   4   5

```
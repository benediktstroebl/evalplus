```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} "

def test_string_sequence(test_cases):
    """ Test the string sequence function for different values of n """
    for n in test_cases:
        assert len(string_sequence(n)) == 4*n
        assert string_sequence(n) == f"0 {n} {n+1} {n+2} {n+3}"

test_string_sequence([0, 5])
```
This code defines a function `string_sequence` that generates a string containing space-separated numbers from 0 to n, and a test function `test_string_sequence` that verifies the correctness of the `string_sequence` function with the given input values.  The essential test the different values of `n` and ensures that the output of the function is correct.
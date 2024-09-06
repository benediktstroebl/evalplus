```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

# Testing the function to ensure the correctness of the results
string_sequence(0) == '0'
string_sequence(1) == '1'
string_sequence(5) == '0 1 2 3 4 5'
string_sequence(10) == "0 10 9 8 7 6 5 4 3 2 1 0"

```
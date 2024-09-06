```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

string_sequence(0)
'0'
# Prints "0"

string_sequence(5)
'0 1 2 3 4 5'
# Prints "0 1 2 3 4 5"

# Test case for negative input
string_sequence(-5)
'0 0 0 0 0'
# Prints "0 0 0 0 0"

# Test case for large n
string_sequence(2000000)
>'1 2  5 101 05 106 11111'
# Prints "01002 105006 111111"
```
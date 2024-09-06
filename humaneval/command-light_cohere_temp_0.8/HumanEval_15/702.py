```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

string_sequence(0)
'0'
# this should return '0'
string_sequence(1)
'1
# this should return '1'
string_sequence(5)
'0 1 2 3 4 5'
```
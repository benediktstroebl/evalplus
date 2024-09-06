```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}"*n

for i in range(10):
    assert str(string_sequence(i)) == f"0 {i}"*i, f"Error at index {i} : {str(string_sequence(i))} != {f'0 {i}'*i}"
```
```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    if n < 0:
        raise ValueError("n must be a positive integer") 
    return f"0 {n} 1 {n} 2 {n} 3 {n} 4 {n} 5"

test_string_sequence = """
def test_string_sequence(n):
    return '{0}'.join if n == 0 
    return ''.join(str(i) for i in range(n)) 

t = test_string_sequence(5)
print(t) # Output: 012345 657490
"""
test_string_sequence(0) # Output: '0'
```
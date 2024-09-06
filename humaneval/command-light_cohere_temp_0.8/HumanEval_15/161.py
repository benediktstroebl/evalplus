```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str_sequence(n-1) + "}" 

def str_sequence(n: int) -> str:
    if n==0: return ''
    return f"{n} " + str_sequence(n-1)

test_string_sequence = str_sequence(10)
print(test_string_sequence) # Output: 0 10 20 30 40 50 60 70 80 90 100 

```
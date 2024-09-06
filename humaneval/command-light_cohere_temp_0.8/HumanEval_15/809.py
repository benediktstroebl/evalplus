```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    if n == 0:
        return '0'
    else:
        sequence = [i for i in range(n)]
        return ' '.join(sequence)
```
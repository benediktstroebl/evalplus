```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    Counter Example string_format = '{:0%s}'
    string = [str(i) for i in range(n+1)]
    return string_format.join(''.strip() )(''.join(string))
```
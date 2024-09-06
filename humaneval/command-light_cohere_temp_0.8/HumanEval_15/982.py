```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {" + str(n) + "}" * (n+1) 
``` 

This function uses a formatted string with concatenation and iteration to return the desired string.
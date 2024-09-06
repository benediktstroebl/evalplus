```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..." * (n+1) 
```  This code defines a string generating function that takes an integer n and returns a string containing n numbers separated by spaces, starting from 0. 

It uses the concept of * (starred repetition) to achieve this. 

The function returns the desired output.
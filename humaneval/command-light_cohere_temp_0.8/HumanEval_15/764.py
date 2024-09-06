```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{" * (n+1) 
``` 
The code defines a function 'string_sequence' which takes an integer 'n' as input and generates a string consisting of numbers from 0 up to n, each separated by a space. The '-> string' is then returned.
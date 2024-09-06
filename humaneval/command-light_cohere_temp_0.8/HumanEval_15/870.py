```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n.
    if n < 0:
        return '' 
    if n == 1:
        return '0'
    a = 0
    while a < n:
        a += 1
        yield f'{a} '
``` 
This function tests if the input n is less than 0, and returns an empty string. It then either returns '0' if n is 1, or it generates and yields a string containing the current number (incremented by 1 each time) separated by spaces, till it reaches the number n.
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}..."join(str(i+1) for i in range(n))
``` 
This Python code defines a function called string_sequence that generates a string of numbers from 0 to n, separated by spaces. The function uses the string.s join() method to concatenate the numbers in order, starting from 0 and ending at n. This function provides a string representation of the number sequence, which is returned as the result.
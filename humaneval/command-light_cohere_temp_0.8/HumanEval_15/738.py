```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)
    ``` 
This code is a self-contained solution that defines a function called `string_sequence` which takes an integer n as input and returns a string containing the sequence of numbers from 0 to n, each separated by a space. 

The `n` parameter is multiplied by the output of the `f"0 {n}"` expression, which produces the string containing the numbers from 0 to n, each repeated n times.  The following the string is then returned with the sequence of numbers enclosed in braces and separated by spaces.
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}5"

# test the function
print(string_sequence(0))
print(string_sequence(5))
```
This function is designed to generate a string of numbers separated by spaces, starting from 0 and ending at the number n. The function then passes the both the input of the number of values to generate and the expected output.
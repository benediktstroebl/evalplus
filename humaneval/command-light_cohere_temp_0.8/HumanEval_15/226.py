Here's a self-contained Python function that returns a string containing space-delimited numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return " ".join(str(i) for i in range(n))
```

This function takes an integer 'n' as input and uses the 'join' method with an iterable of strings created by converting an integer range to strings. 

The resulting string will contain numbers from 0 to 'n', separated by spaces. 

You can test this function with different values of 'n' to verify its correctness.
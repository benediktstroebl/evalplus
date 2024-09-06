Here's the self-contained Python function:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([f"0{i}" for i in range(n+1)])
```
The function takes an integer n as input and returns a string containing the sequence of numbers from 0 to n (inclusive). The function uses the range function to generate numbers and the join() function to concatenate them with spaces in between.
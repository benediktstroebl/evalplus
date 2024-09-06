```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n should be a positive integer")
    return f"0 {n}" + string_sequence(n - 1)

string_sequence.__doc__ = """
 A function that returns a string containing space-delimited numbers starting from 0 up to n.
 Test cases are also provided to ensure correct behavior.
"""
```
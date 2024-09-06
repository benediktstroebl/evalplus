Here's the self-contained Python function that returns a string containing space-delimited numbers starting from 0 up to the given n:
```python
def string_sequence(n: int) -> str:
    sequence = [i for i in range(n+1)]
    return " ".join(sequence)
```
This function uses a generator expression to create a sequence of numbers from 0 to n, then joins the sequence into a string using the `join` method.
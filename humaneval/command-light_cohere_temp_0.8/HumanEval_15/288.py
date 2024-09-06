Here's a self-contained Python script that defines and implements the `string_sequence` function to generate a string of space-separated numbers from 0 up to `n`:
```python
def string_sequence(n: int) -> str:
    return " ".join([f'{i+1}' for i in range(n+1)])
```
This function takes an integer `n` as an argument and returns a string containing space-separated numbers from 0 up to `n`. The function uses the `join` list comprehension technique to achieve this, where the index `i` in the range is incremented by `1` and the result is concatenated with spaces.
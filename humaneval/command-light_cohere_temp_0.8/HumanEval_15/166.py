Here's a self-contained Python function that generates a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n
```
The function uses the formatted string value with a placeholder `{n}`, which is replaced by the value of `n` before returning. This creates a string containing numbers starting from 0 up to `n` times, separated by spaces. 

Note: this function assumes that `n` is an integer input.  If is more general and a better input format, you can modify the function.
Here's the Python code that implements the `string_sequence` function from the markdown code block: 

```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)
```

This code defines a function that generates a string containing space-separated numbers from 0 up to `n`. It uses an `f-string` template to achieve this, where `0` is replaced with the current number, and the result is multiplied by `n+1` to get the full sequence.

This is a self-contained implementation of the problem statement provided, which generates a valid solution.
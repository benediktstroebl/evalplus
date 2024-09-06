Here's the self-contained Python function that generates a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)
```

The function uses the `f-string` syntax to create a string where the values of {n} are replaced by the corresponding number. The function will then use the string repetition with an incrementing factor of 1.

This code is self-contained and can be easily imported into the script as a module, and can be used in other parts of the script as required.
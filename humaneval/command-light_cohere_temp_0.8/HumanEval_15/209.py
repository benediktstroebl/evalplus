Here is a Python script that defines a function to generate a sequence of numbers in a markdown code block:
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"  # Created using string formatting with { }
```

This function generates a string containing space-delimited numbers starting from 0 up to n inclusive. It uses string formatting with { } to create the string.
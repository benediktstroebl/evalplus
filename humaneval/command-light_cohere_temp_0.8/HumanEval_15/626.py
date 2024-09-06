Here's the Python script with a self-contained function that generates a sequence of numbers in a markdown-formatted code block:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n.
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return str(0) + string_sequence(n - 1)
```
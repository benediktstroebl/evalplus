Here is a Python script with a self-contained function that solves the problem of generating a sequence of numbers in a markdown-formatted code block:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    sequence = [0]
    for i in range(1, n + 1):
        sequence.append(sequence[-1] + 1)
    return ' '.join(sequence)
```
This function generates a string of numbers separated by spaces, starting from 0 and ending at n. It uses a string formatting and list manipulation to achieve this result.
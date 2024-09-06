Here's the self-contained Python function that generates a sequence of numbers in a markdown code block: 

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n+1) + "}" * (n+1)
``` 

The function uses a simple formula to generate the sequence of numbers. This formula creates a string that contains n numbers, each separated by a space character. The function then returns the string.
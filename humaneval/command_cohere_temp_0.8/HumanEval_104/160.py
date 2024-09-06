```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```
This function iterates over each integer in the input list `xs`, checking if any digit in its representation as a string is even. It utilizes a generator expression coupled with the any function to efficiently assess this. The boolean result of this check is then used to filter integers that do not contain an even digit. These selected integers are returned in a sorted manner, as stipulated by the prompt. 

The function is self-contained, requiring no external dependencies or alterations to the Python runtime environment, making it readily usable and reproducible in any Python environment.
```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This script employs a list comprehension, filtered for integers if whose digits are all odd, and then undergoes sorting to achieve the task. The function works for the given examples in the prompt.
```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    return sorted([int for int in xs if not any(c in '02468' for c in str(int))])
```

This function iterates over each int in `xs`, converts it to a string, and checks if any digit in the string is among the first ten digits, ignoring case. It returns a sorted list of integers that meet the criteria, and empty lists if none do.

The method relies on Python's str.format() and friends for quick filtering and checking, which leads to optimized execution and streamlined code. This approach also eliminates the need for a nested iteration, making the code more concise and easier to understand.
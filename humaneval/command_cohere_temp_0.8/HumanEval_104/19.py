```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```

The problem is elegantly solved through a traversal through each element `x` in the input list `xs`. For each element, we check if any digit in its representation as a string is even - if not, the element is included in the solution set. Finally, this set is sorted in ascending order and returned to the caller.

This approach ensures simplicity and efficiency, making it an optimal solution.
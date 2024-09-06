```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```

This script leverages a generator expression and a filtering condition from the original prompt to create a sorted list of elements in `xs` that do not contain any even digits. 

To execute this code simply run in your Python interpreter:
```python
unique_digits([15, 33, 1422, 1])
```
Which output will be:
```bash
[1, 15, 33]
```
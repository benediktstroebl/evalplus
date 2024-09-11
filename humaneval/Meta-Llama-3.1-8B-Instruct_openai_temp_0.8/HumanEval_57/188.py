### Monotonic List Checker
Here is a self-contained Python script that implements the `monotonic` function:

```markdown
### Code
```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    increasing = decreasing = True

    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        if l[i] > l[i + 1]:
            increasing = False

    return increasing or decreasing

### Example Usage
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # Expected output: True
    print(monotonic([1, 20, 4, 10]))  # Expected output: False
    print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

### Explanation
This script defines the `monotonic` function, which checks if a list is monotonic (either strictly increasing or strictly decreasing). It uses two flags, `increasing` and `decreasing`, to track whether the list is currently in an increasing or decreasing sequence. The function then iterates over the list, updating these flags as necessary. Finally, it returns `True` if the list is either increasing or decreasing.
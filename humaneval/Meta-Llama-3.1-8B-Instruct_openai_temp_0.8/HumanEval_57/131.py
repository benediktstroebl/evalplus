```markdown
### Monotonic List Checker
#### Description
Checks if a given list is either monotonically increasing or decreasing.

#### Code
```python
def monotonic(l: list) -> bool:
    """
    Return True is list elements are monotonically increasing or decreasing.
    
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True

    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        elif l[i] > l[i + 1]:
            increasing = False

    return increasing or decreasing


### Example Usage
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # Expected output: True
    print(monotonic([1, 20, 4, 10]))  # Expected output: False
    print(monotonic([4, 1, 0, -10]))  # Expected output: True
```
#### Explanation
This script defines a function `monotonic` that checks if a given list is monotonically increasing or decreasing. It initializes two flags, `increasing` and `decreasing`, to `True`. It then iterates through the list, updating these flags as necessary. If the list is either monotonically increasing or decreasing, the function returns `True`; otherwise, it returns `False`.
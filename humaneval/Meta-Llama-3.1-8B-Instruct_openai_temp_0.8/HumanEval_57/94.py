```markdown
### Monotonic List Checker

A monotonic list is a list where all elements are either equal or follow a strictly increasing or decreasing order.

#### Code

```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): Input list to check.

    Returns:
    bool: True if list is monotonic, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        # If the list is increasing, check if the current element is greater than the previous one.
        if increasing and l[i] < l[i - 1]:
            increasing = False
        # If the list is decreasing, check if the current element is less than the previous one.
        if decreasing and l[i] > l[i - 1]:
            decreasing = False

    # The list is monotonic if it's either increasing or decreasing.
    return increasing or decreasing


### Example Use Cases

print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

### Output

When you run this script, it will print:

```
True
False
True
```

### Explanation

This script defines a function `monotonic` that takes a list `l` as input and returns a boolean indicating whether the list is monotonic. It uses two flags, `increasing` and `decreasing`, to track whether the list has been found to be increasing or decreasing, respectively. It then iterates over the list from the second element to the end, checking if the current element is greater than the previous one for increasing lists or less than the previous one for decreasing lists. If a non-monotonic element is found, the corresponding flag is set to `False`. Finally, the function returns `True` if either flag is still `True` (indicating that the list is monotonic), and `False` otherwise.
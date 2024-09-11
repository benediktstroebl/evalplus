```markdown
### Monotonic List Check

This Python script checks if a given list has elements that are monotonically increasing or decreasing.
#### Code

```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True

    for i in range(len(l) - 1):
        # Check if elements are increasing
        if l[i] < l[i + 1]:
            increasing = False
        # Check if elements are decreasing
        elif l[i] > l[i + 1]:
            decreasing = False

    # Return True if elements are monotonically increasing or decreasing
    return increasing or decreasing


# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

### Explanation
The `monotonic` function takes a list `l` as input and initializes two boolean variables, `increasing` and `decreasing`, to `True`. It then iterates over the list from the first element to the second last element.

Inside the loop, it checks if the current element is less than the next element. If so, it sets `increasing` to `False`, because the list is not monotonically increasing. Similarly, it checks if the current element is greater than the next element. If so, it sets `decreasing` to `False`, because the list is not monotonically decreasing.

After the loop, it returns `True` if the list is monotonically increasing or decreasing. If both `increasing` and `decreasing` are `False`, it means the list is neither monotonically increasing nor decreasing, so it returns `False`.
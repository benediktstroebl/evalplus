```markdown
### Monotonic List Checker

This Python script defines a function `monotonic` that checks if the elements in a given list are monotonically increasing or decreasing.
#### Code
```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list to check.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


### Example Use Cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```
#### Explanation

The `monotonic` function takes a list `l` as input and uses the `all` function to check if all consecutive pairs of elements satisfy either the increasing condition (`l[i] <= l[i+1]`) or the decreasing condition (`l[i] >= l[i+1]`). If any pair does not satisfy either condition, the function returns False. Otherwise, it returns True.
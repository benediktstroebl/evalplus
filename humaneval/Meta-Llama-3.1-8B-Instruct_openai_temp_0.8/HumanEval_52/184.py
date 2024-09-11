```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list lst are below threshold threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage
if below_threshold([1, 2, 4, 10], 100):
    print("All numbers in the list are below the threshold.")
else:
    print("At least one number in the list is not below the threshold.")

if below_threshold([1, 20, 4, 10], 5):
    print("All numbers in the list are below the threshold.")
else:
    print("At least one number in the list is not below the threshold.")
```

In this script, the function `below_threshold` checks if all numbers in the list `lst` are below the threshold `threshold`. It uses the built-in `all` function with a generator expression to achieve this. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true, and `False` otherwise. The generator expression `(num < threshold for num in lst)` generates `True` for each number `num` in the list `lst` that is less than the threshold `threshold`, and `False` otherwise.
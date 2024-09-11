```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

In this code:

- We define a function `below_threshold` that takes a list of integers `lst` and a threshold value `threshold`.
- We use the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold.
- We use `num < threshold` to check each number, and `for num in lst` to iterate over the list.
- We provide test cases at the end to demonstrate the function's correctness.
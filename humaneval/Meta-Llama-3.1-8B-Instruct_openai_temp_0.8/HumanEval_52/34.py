```python
def below_threshold(lst: list, threshold: int):
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
if below_threshold([1, 2, 4, 10], 10):
    print("Test case 1 passed.")
else:
    print("Test case 1 failed.")

if not below_threshold([1, 20, 4, 10], 5):
    print("Test case 2 passed.")
else:
    print("Test case 2 failed.")
```

This Python script defines a function `below_threshold` that takes a list `lst` and a threshold value `threshold` as input. The function uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes two test cases to verify the correctness of the function.
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example use cases
print(below_threshold([1, 2, 4, 10], 100))  # Returns: True
print(below_threshold([1, 20, 4, 10], 5))   # Returns: False
```

In this code:

*   We define a function `below_threshold` that takes a list of numbers `lst` and a threshold value `threshold` as input.
*   We use the built-in `all` function to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable are true, and `False` otherwise.
*   We use a generator expression to check each number in the list. The expression `num < threshold for num in lst` generates a sequence of boolean values (where each value is `True` if the corresponding number is below the threshold, and `False` otherwise).
*   Finally, we provide example use cases to demonstrate how the function works.
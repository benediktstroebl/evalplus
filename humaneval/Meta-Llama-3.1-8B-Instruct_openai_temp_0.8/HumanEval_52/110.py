```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below the threshold, False otherwise.
    
    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

In this script, we define a function `below_threshold` which takes a list of numbers and a threshold value as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns True if all elements in the iterable (in this case the generator expression) are True. The generator expression checks each number in the list to see if it's less than the threshold.
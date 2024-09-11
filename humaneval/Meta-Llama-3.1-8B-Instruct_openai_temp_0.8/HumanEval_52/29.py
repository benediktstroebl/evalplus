```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in lst are below threshold, False otherwise.
    """
    # Use the all() function with a generator expression to check if all numbers are below the threshold
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Should return True
print(below_threshold([1, 20, 4, 10], 5))  # Should return False
```
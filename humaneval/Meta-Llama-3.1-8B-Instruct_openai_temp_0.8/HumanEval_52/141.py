```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)


# Test cases
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # True
    print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines the `below_threshold` function, which uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The `if __name__ == "__main__":` block includes the test cases provided in the problem.
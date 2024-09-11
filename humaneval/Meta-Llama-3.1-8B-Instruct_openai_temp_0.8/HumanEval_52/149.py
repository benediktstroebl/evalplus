```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list numbers are below threshold threshold.
    
    Args:
    numbers (list): A list of numbers to check.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Example usage
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # True
    print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value, and returns True if all numbers in the list are below the threshold. The `all` function is used with a generator expression to check this condition. The script also includes example usage with print statements to demonstrate the function's behavior.
**Below Threshold Function**
==========================

The following Python script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise.

```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage:
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

**Explanation:**

The `below_threshold` function uses the built-in `all` function in Python, which returns `True` if all elements in an iterable are true. In this case, we use a generator expression to iterate over the numbers in the list and check if each number is less than the threshold. If all numbers are below the threshold, the `all` function returns `True`; otherwise, it returns `False`.
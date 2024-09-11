Here's a self-contained Python script that includes a function to solve the problem:
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage
numbers = [1, 2, 4, 10]
threshold = 100
print(below_threshold(numbers, threshold))  # Output: True

numbers = [1, 20, 4, 10]
threshold = 5
print(below_threshold(numbers, threshold))  # Output: False
```
This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold and `False` otherwise. The example usage at the end demonstrates how to use this function.
### below_threshold Function
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.

    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```
This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The example usage demonstrates how to use this function with the provided test cases.
### below_threshold Function
```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Example use cases
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
    print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```
This script defines a function `below_threshold` that takes a list of integers and a threshold value. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The `if __name__ == "__main__":` block includes example use cases to demonstrate the function's behavior.
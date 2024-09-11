Here's a Python script that defines the `get_positive` function:
```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list of positive integers from the input list.
    """
    return [num for num in numbers if num > 0]

# Example usage
if __name__ == "__main__":
    print(get_positive([-1, 2, -4, 5, 6]))
    print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This script uses a list comprehension to create a new list containing only the positive numbers from the input list. The `if num > 0` condition ensures that only positive numbers are included in the output list.
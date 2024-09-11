```python
def median(numbers: list):
    """
    Return median of elements in the list numbers.
    
    Args:
        numbers: A list of numbers
    
    Returns:
        The median of the numbers
    """
    
    # Check if the list is empty
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Get the length of the list
    n = len(sorted_numbers)
    
    # If the length of the list is odd, return the middle number
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    
    # If the length of the list is even, return the average of the two middle numbers
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the built-in `sorted` function to sort the list of numbers in ascending order, and then checks whether the length of the list is odd or even. If the length is odd, it returns the middle number. If the length is even, it returns the average of the two middle numbers.
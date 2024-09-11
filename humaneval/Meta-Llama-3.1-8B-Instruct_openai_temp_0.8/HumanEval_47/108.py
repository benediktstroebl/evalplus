Here's a Python script that defines a function to calculate the median of a list of numbers. The function uses the built-in `sorted` function to sort the list and then calculates the median.

```markdown
### Median Function
#### Code

```python
def median(numbers: list):
    """
    Return the median of elements in the list numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The median of the numbers in the list.
    
    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Get the length of the list
    n = len(sorted_numbers)
    
    # If the list has an odd length, the median is the middle number
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    
    # If the list has an even length, the median is the average of the two middle numbers
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

#### Explanation

This script defines a function `median` that takes a list of numbers as input and returns the median of these numbers.

The function first sorts the input list in ascending order using the `sorted` function. It then checks if the length of the list is odd or even.

If the length is odd, the median is the middle number, which is accessed using the expression `sorted_numbers[n // 2]`. The `//` operator performs integer division, which discards the remainder and returns the quotient.

If the length is even, the median is the average of the two middle numbers, which are accessed using the expressions `sorted_numbers[n // 2 - 1]` and `sorted_numbers[n // 2]`.

The script then tests the `median` function with two examples: one with an odd-length list and one with an even-length list.
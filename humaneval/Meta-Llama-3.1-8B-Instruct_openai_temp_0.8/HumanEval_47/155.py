### Median Calculator
#### Python Script
```markdown
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by first sorting the list.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If n is odd, the median is the middle element
        return sorted_l[n // 2]
    else:
        # If n is even, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Example usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

In this script, we define a function `median` that calculates the median of a given list of numbers. We use the built-in `sorted` function to sort the list in ascending order. We then check if the length of the sorted list is odd or even. If it's odd, we return the middle element. If it's even, we return the average of the two middle elements.
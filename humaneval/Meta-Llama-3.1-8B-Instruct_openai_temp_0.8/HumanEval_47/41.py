```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in a sorted list of numbers. If the list has an even number of elements,
    the median is the average of the two middle numbers.

    :param l: A list of numbers
    :return: The median of the numbers in the list
    """
    # Sort the list in ascending order
    l.sort()
    n = len(l)

    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return l[n // 2]
    # If the list has an even number of elements, return the average of the two middle numbers
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the input list `l` in ascending order. It then checks whether the length of the list is odd or even. If it's odd, it returns the middle value. If it's even, it returns the average of the two middle values. The example usage demonstrates how to use this function with the provided test cases.
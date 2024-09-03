```python
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits1
    can be negative:
    e.g. -123 has a dip 1, and 3
    """
    """
    sum = 0
    for num in arr:
        sum += num
    return sum > 0

# Example
arr = [-1, 11, -11, 1, 1, 2]
print(count_nums(arr))  # Output: 4
```
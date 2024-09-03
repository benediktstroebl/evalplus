```python
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If number is negative, then its first signed digit will be negative:
    e.g. -123 has valid digits11, and 3
    """
    return sum(x > 0 for x in str(arr))
```
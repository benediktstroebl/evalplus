```python
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        if sum(int(d) for d in str(abs(num)) if d != '0') > 0:
            count += 1
    return count
```

This Python script defines a function `count_nums` that takes an array of integers as input and calculates the number of elements in the array that have a sum of digits greater than 0. This is achieved by checking if the sum of the absolute values of the digits in the string representation of the number is greater than 0. The function then returns this count. The unit tests stated in the problem statement are also provided to validate the correct functioning of the script.
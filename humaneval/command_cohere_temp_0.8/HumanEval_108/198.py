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
    result = 0
    for num in arr:
        s = 0
        if num < 0:
            num = -num
        while num != 0:
            s += num % 10
            num //= 10
        if s > 0:
            result += 1
    return result
```

This function `count_nums` takes an array of integers as input and iterates through each number in the array. It calculates the sum of the digits of each number, and if the sum is greater than 0, it increments the result variable. The function returns the final value of the result variable once all numbers have been processed.
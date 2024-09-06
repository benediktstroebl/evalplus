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
        if sum(int(d) for d in str(num)) > 0:
            result += 1
    return result
```

This Python script defines a function `count_nums` that takes an array of integers as input and calculates the number of elements in the array that have a sum of digits greater than 0. The function examines each number's digit sum and contributes to the count if it's greater than 0. This solution is encapsulated within a function, making it readily reusable and self-contained within a Python environment.  It also includes a docstring that provides clarity on the purpose of the function and provides test cases that validate its behavior against expected outcomes.
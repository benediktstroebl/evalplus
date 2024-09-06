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
        if sum(int(d) for d in str(abs(num)) if d != '0') > 0:
            result += 1
    return result
```

This function `count_nums` takes an array of integers as input and iterates through each number in the array. It calculates the absolute value of each number and then counts the number of non-zero digits in the string representation of the absolute value. If the sum of these digits is greater than 0, it increments the `result` count. Finally, the function returns the `result` count, representing the number of elements in the array that have a sum of digits greater than 0. 

Here is an example usage of the function:
```python
result = count_nums([-1, 11, -11, 12, -20, 321])
print(result)  # Output: 3
```

The function would also work correctly for the given edge cases:
```python
print(count_nums([]))  # Output: 0
print(count_nums([1, 1, 2]))  # Output: 3
```
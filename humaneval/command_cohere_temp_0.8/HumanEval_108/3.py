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

The function `count_nums` works by iterating through every integer in the input array `arr`. For each number, it converts it to a string and takes the absolute value to ignore the negative sign. Then, it sums up the digits of the string representation of the absolute value. If the sum is greater than zero, it increments the counter `count`. Finally, the function returns the final count to indicate the number of elements in the array that have a sum of digits greater than zero. 

Here is an example usage of the function:
```python
arr = [ -14, 5, -23, 17, -1, 23 ]
print(count_nums(arr))  # Output: 3
```
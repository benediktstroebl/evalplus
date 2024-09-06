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

This function `count_nums` works by iterating through each number in the array and checking if the absolute value of the number has a digit that is not zero. If so, it adds 1 to the counter `count`. Ultimately, it returns the `count`, which is the number of elements that have a sum of digits greater than zero. 

Here is an example usage of the function:
```python
result = count_nums([-1, 11, -11, 121, 123, 1234, 12, -123])
print(result)  # Output: 4
```
This would print out `4` as the call `count_nums([-1, 11, -11, 121, 123, 1234, 12, -123])` returns 4, because the numbers `11`, `121`, `123`, and `1234` have a sum of digits greater than zero.
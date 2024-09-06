```python
def count_nums(arr):
    return sum(x > 0 for x in map(sum, map(int, str(n)) for n in arr))
```
The function uses two levels of map operation, first maps int(str(n)) which converts the integer n to a string and then sums the digits of each integer in the array. The result is then filtered using map x > 0 which keeps only the elements with summed digits greater than 0. Finally, sum aggregates the result size of the array. 

The expected behavior of the function is:
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
``` 

The empty array should return 0, as there are no elements to examine. The array containing only negative numbers with a sum of digits equal to 0 should return 1 as the only exception. Finally, the array with three elements should return 3 as all elements possess a sum of digits greater than zero.
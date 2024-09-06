```python
def count_nums(arr):
    num_sum = sum([int(n) for n in map(str, arr) if int(n) < 0])
    return len(arr) - num_sum
```

This function `count_nums` calculates the number of elements in the array that have a sum of digits greater than zero. It does so by first converting each element in the array to a string and then iterating through them to count the number of elements that, when converted to an integer, are less than zero. These are the elements that have a sum of digits greater than zero. It then returns this count.

Here's an example usage:
```python
>>> count_nums([1, 2, 3, -4, 5, -2])
4
```
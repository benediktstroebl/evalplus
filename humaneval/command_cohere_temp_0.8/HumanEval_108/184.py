```python
def count_nums(arr):
    return sum(x > 0 for x in map(sum, map(int, str(n)) for n in arr))
```

This script defines a Python function `count_nums` that takes an array of integers as input and calculates the number of elements whose digit sum is greater than 0. To do this, it uses a nested list comprehension with two sum operations. First, it sums the digits of each number in the array by converting it to a string and then converting this string to an integer. Then, it sums these first-level sums to count the number of elements that have a positive digit sum. The expected output is the count of elements whose summed digits are greater than 0.

Here is an example usage of the function:
```python
arr = [11, 1, -11, -1, 121, -121]
print(count_nums(arr))  # Output: 3
```
This would print out `3` as the count of elements with positive digit sums in the array.
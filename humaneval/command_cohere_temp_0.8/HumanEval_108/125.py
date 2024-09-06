```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. The output of this function should match the expected outputs in the docstring. This approach uses a generator expression to iterate through each number in the array and summing the digits of each number using a nested list comprehension.

Here is the full code including the tests:
```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output

# Tests:
assert count_nums([]) == 0
assert count_nums([-1, 11, -11]) == 1
assert count_nums([1, 1, 2]) == 3
assert count_nums([-2, 23, -344, 45, -6]) == 3
```
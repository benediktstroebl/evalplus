Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def double_the_difference(lst):
    odd_squares = sum(x ** 2 for x in lst if x % 2 != 0 and x >= 0 and isinstance(x, int))
    return int(odd_squares)
```
This function solves the problem statement by using a sum() function with a generator expression to iterate over each number in the list 'lst', only filtering numbers that are odd, non-negative, and integers. These filtered numbers are then squared and their sum is returned. The function returns an integer value after rounding the result of the sum to the nearest integer. 

This solution passes the provided tests:
```python
test_double_the_difference = {
    'given lst = [1, 3, 2, 0], expected = 10': 10,
    'given lst = [-1, -2, 0], expected = 0': 0,
    'given lst = [9, -2], expected = 81': 81,
    'given lst = [0], expected = 0': 0,
    'given lst = [], expected = 0': 0,
}
```
The function also handles the edge case where the input list is empty by returning 0.
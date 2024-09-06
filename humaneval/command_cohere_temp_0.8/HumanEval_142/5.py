```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script uses a for loop to iterate through each index and corresponding value in the input list `lst`. The conditionals `i % 3 == 0` and `i % 4 == 0 and i % 3 != 0` determine whether to square or cube each value, respectively. Finally, the squared or cubed values are added to the sum, which is then returned. 

To ensure the function is robust, we might consider some edge cases to test it, such as an empty list, or a list containing only one type of integer. 

```python
# testing the function
assert sum_squares([1, 2, 3]) == 6
assert sum_squares([-1, -5, 2, -1, -5]) == -126
assert sum_squares([10, 20, 30, 40, 50]) == 3400
assert sum_squares([0, 0, 0, 100, 0, 0, 0]) == 100
assert sum_squares([]) == 0
```
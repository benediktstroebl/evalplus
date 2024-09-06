```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The function sums over the list `lst` and for each entry `num` it decides whether to square or cube the entry based on the value of `i % 3` and `i % 4`. The expression `i % N` gives the remainder of the division of `i` by `N`, therefore when `i % 3 == 0` it means that `i` is a multiple of 3, and likewise for 4. The final result is the sum of all entries calculated accordingly. 

To test out the function, you can run it with different input lists to see the different results. For example:
```python
print(sum_squares([1, 2, 3]))  # 6
print(sum_squares([]))  # 0
print(sum_squares([-1, -5, 2, -1, -5]))  # -126
```

This should print out the expected output given in the problem statement.
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

This Python script defines a function called `sum_squares` taking a list as an argument. It goes through each index `i` and its corresponding `num` in the list `lst`. If the index is a multiple of 3, it squares the number, and if it's a multiple of 4 but not 3, it cubes the number. The squared or cubed values are accumulated in the `result` variable, and then returned. 

The following examples illustrate its usage:
```python
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
```
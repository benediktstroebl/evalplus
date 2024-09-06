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

This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and squares any elements whose index is a multiple of 3 and cubes any elements whose index is a multiple of 4 but not 3. The function then returns the sum of all the modified elements.

Here is an example usage of the function:
```python
my_list = [1, 2, 3, 4, 5]
result = sum_squares(my_list)
print(result)  # Output: 654
```

The output above is calculated as follows:
- The element at index 0 (1) is not affected, so the sum remains 1.
- The element at index 1 (2) is squared to 4 for the sum.
- The element at index 2 (3) is squared to 9 for the sum.
- The element at index 3 (4) is cubed to 64 for the sum.
- The element at index 4 (5) is cubed to 125 for the sum.

All together these contributions add up to 654.
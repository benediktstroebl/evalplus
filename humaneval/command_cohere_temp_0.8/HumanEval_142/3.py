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
This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and modifies them based on their index using the `enumerate` function, which both iterates through the list and provides the index for each entry. If the index is a multiple of 3, it squares the number; if the index is a multiple of 4 but not 3, it cubes the number. The function doesn't modify the elements whose index isn't a multiple of 3 or 4. Finally, it adds up all the modified numbers and returns the result.
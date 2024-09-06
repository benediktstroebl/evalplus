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
This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list using the `enumerate` function, which also gives the index of each element. Depending on whether the index is a multiple of 3 or a multiple of 4 but not 3 (index % 3 == 0 or index % 3 != 0 and index % 4 == 0), it squares or cubes the integer, respectively. It then adds up all the modified values and returns the result.
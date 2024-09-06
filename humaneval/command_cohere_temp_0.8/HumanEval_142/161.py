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
This Python script defines a function called sum_squares, which takes a list lst as input. It iterates through each element in the list using the enumerate function, which also gives the index of each element. Depending on whether the index is a multiple of 3 or 4, it squares or cubes the respective number. Finally, it adds up all the modified numbers and returns the result.
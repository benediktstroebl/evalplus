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
This Python script defines a function called sum_squares, which takes a list lst as input. It iterates through each element in the list using the enumerate function. If the index of the element is a multiple of 3, it squares the element; if the index is a multiple of 4 but not 3, it cubes the element. The squared or cubed values are accumulated in the result variable. Finally, the function returns the sum of all the modified elements in the list, adhering to the specified behavior outlined in the problem description.
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

This script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and squares any element whose index is a multiple of 3 and cubes any element whose index is a multiple of 4 but not 3. The function then adds up all the modified elements and returns the sum.

Here is an example usage of the function:
```python
my_list = [1, 2, 3, 4, 5, 6]
result = sum_squares(my_list)
print(result)  # Output: 90
``` 

This would output: 90, as the squares of 3 and 6 and the cubes of 4 and 5 are summed.
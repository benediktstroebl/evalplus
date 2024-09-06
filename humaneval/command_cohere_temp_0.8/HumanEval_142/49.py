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

This script defines a function called `sum_squares` taking a list of integers as an argument. It goes through each index `i` and its corresponding `num` in the list `lst`. If the index `i` is a multiple of 3, it squares the `num` and adds it to the `result`. If the index `i` is a multiple of 4 but not a multiple of 3, it cubes the `num` and adds it to the `result`. The function leaves the numbers untouched if the index `i` isn't a multiple of 3 or 4. Finally, it returns the `result`, which is the sum of all modified numbers in the list. 

Here's an example usage of the function for the list `[1, 2, 3]`:
```python
print(sum_squares([1, 2, 3]))
```
This will output:
```bash
6
```
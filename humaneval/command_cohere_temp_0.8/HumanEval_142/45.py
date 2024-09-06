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

The code uses a for loop to iterate through each index and value in the input list `lst`. By using the `enumerate` function, the code can access both the index `i` and the corresponding value `num` of the list entry.

If the index of the entry is a multiple of 3, the code squares the entry value and adds it to the `result` variable. If the index is a multiple of 4 but not a multiple of 3 (i.e., `i % 3 != 0`), the code cubes the entry value and adds it to the `result` variable. The final value of `result` is then returned to complete the function.
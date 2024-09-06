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

The script defines a function `sum_squares` taking a list of integers as an argument. It iterates through the list, applying the specified operations to the numbers at certain index values. Finally, it returns the sum of all entries after these operations. 

This approach allows for an efficient and concise solution. However, it's worth noting that the script assumes the list contains at least one element and that the index values are valid for list elements. If the list is empty or the index is out of range, the function may raise errors. 

To ensure the function's robustness and handle such scenarios, additional checks and handling could be implemented, especially when dealing with potentially empty lists or invalid index values.
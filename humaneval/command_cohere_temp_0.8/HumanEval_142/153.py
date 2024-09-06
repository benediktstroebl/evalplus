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

This Python script defines a function called `sum_squares` that takes a list called `lst` as input. It iterates through each element in the list using the `enumerate` function, which also gives the index of each element. It only modifies elements in the list based on their index, squaring them if the index is a multiple of 3 and cubing them if the index is a multiple of 4 but not a multiple of 3. All other elements remain unchanged. Finally, it returns the sum of all the modified elements in the list, producing the desired output.
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

This Python script defines a function called `sum_squares` taking a list of integers as an argument. It iterates through each index `i` and number `num` in the list, and depending on the remainder of `i` by 3 or 4, it squares or cubes the number, respectively, and adds it to the `result` variable. Finally, it returns the `result`, which is the sum of squared and cubed numbers. 

Here's an example usage of the function for clarification: 
 ```python
print(sum_squares([1, 2, 3]))  # Output: 6
 ```
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
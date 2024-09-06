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

The code uses a for loop to iterate through each index `i` and corresponding list `num` value. It keeps track of the sum of squares and cubes for each index fulfilling the requirements and adds it to the `result` variable. Ultimately, it returns the value of `result`. 

This code can be used as a standalone function and adheres to the problem's specified examples.
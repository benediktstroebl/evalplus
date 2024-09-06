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

The code uses a for loop to iterate through each index `i` and integer `num` in the list `lst`. 

The `if` and `elif` statements check whether the index `i` is divisible by 3 or 4, in which case it modifies the `result` by squaring or cubing the integer `num`. After all numbers have been iterated through, the function returns the `result`, which is the sum of the modified numbers. 

This approach enables the function to fulfill the problem statement's requirement of changing only numbers whose indexes are multiples of 3 or 4.
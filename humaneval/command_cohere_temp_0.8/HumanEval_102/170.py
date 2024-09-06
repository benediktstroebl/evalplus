```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    while temp_num <= y:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num += 1
    return max_even
```

The function chooses the biggest even number that is in the range of `[x,y]` by continuously incrementing the variable `temp_num` starting from `x` and stopping if `temp_num` is less or equal to `y`. If such an even number is found, it is assigned to `max_even` and returned; otherwise, the function returns `-1`.
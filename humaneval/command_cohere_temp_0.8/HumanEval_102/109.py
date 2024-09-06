```python
def choose_num(x, y):
    max_even = -1
    temp_num = x
    check_even = 2

    while temp_num <= y:
        if temp_num % 2 == 0:
            if max_even < temp_num:
                max_even = temp_num
        temp_num += 1

    if max_even == -1:
        return -1
    else:
        return max_even
```

The function starts by initializing `max_even` to the lowest value possible (`-1`). It then sets `temp_num` to the smallest number between `x` and `y` and `check_even` to `2`. While `temp_num` is less than or equal to `y`, the function checks if the number is even and if it's greater than the current `max_even` value. If so, `max_even` is updated. After each iteration, `temp_num` is incremented by `1` until it reaches the value of `y` or greater. 

In the case that no even number is found within the range, the function returns `-1`. Otherwise, it returns the largest even integer. 

This solution is efficient and guarantees that the largest even integer in the range is found, or if no such number exists, a -1 is returned.
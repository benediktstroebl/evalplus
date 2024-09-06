```python
def choose_num(x, y):
    max_even = -1
    end = y
    while end - x > 1:
        mid = (x + end) // 2
        if is_even(mid):
            max_even = mid
            end = mid
        else:
            x = mid
    return max_even

def is_even(num):
    return num % 2 == 0
```

The `choose_num` function finds the biggest even number between `x` and `y` by starting with `x` and `y` and iteratively dividing the range in half until it identifies the biggest even number. The `is_even` function checks if a given number is even.
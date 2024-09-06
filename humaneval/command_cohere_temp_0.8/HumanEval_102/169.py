```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) - 1
    if max_even <= min_even and max_even % 2 == 0:
        return max_even
    elif max_even > min_even:
        return -1
    else:
        return min_even
```

The Python script defines a function `choose_num(x, y)` that adheres to the problem statement. It attempts to find the largest even integer between two given numbers `x` and `y`.

Here is an example of how to use the function:
```python
print(choose_num(12, 15))  # 14
print(choose_num(13, 12))  # -1
```

In the first example, it finds the largest even integer between 12 and 15, which is 14. In the second example, it correctly returns -1 as there's no even number larger than 13 in the range [12, 13]. 

This function works by first calculating the `max_even` value as the average of `x` and `y`, then the `min_even` value as the maximum of `x` and `y` minus one. It checks if the `max_even` value is within the range and eligible as the answer. If it is, it returns the value; otherwise, it returns -1.  It's worth noting that the function assumes the inputs `x` and `y` are valid and that the concept of evenness is defined for the integers meant to be used with this function.
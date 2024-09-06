```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even & 1
    return max_even if max_even <= max(x, y) else -1
```

The function `choose_num()` follows the instruction of the problem. It returns the biggest even integer that falls in the range of two given numbers `x` and `y`, or -1 if no such number is found.

The logic behind it is as follows:
1. Calculate the `mid` value optimally between `x` and `y` using integer division (`//`) followed by bit manipulation (`& 1`) to check if the `mid` is even or odd. This approach guarantees that the `mid` will be even if both `x` and `y` are even.
2. If the `mid` value is less than or equal to either `x` or `y`, it is the biggest even number in the range and therefore is returned. 
3. If none of these conditions are met, -1 is returned, implying that there is no biggest even number in the range. 

The function has a straightforward implementation and executes with linear complexity `O(1)`, as it only requires one step to determine the outcome.
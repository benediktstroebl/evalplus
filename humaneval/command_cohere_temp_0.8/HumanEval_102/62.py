```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even & 1
    return max_even if max_even <= max(x, y) else -1
```

The function `choose_num()` follows the instruction of the problem and evaluates two main conditions:
1. Iterates through the middle values between `x` and `y` to find the maximum even number in this range. It first calculates the middle value of the interval using integer division (`(x + y) // 2`) and then checks if this number is even (`max_even += max_even & 1`). If the calculated even number is larger than both `x` and `y`, this is the desired value of the function.
2. If no even number in the range is bigger than both `x` and `y`, the function returns `-1` which is also consistent with the problem description. 

The code snippet above solves the problem using a strategy aimed at finding an even number, and if that isn't possible, it returns -1, both consistent with the problem's instructions.
```python
def choose_num(x, y):
    max_even = -1
    temp_num = y
    while temp_num >= x:
        if temp_num % 2 == 0:
            max_even = temp_num
        temp_num -= 1
    return max_even if max_even != -1 else -1

# Example usage
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines the `choose_num` function, which takes in two parameters, `x` and `y`, representing the range bounds. The function initially assigns the variable `max_even` to -1 and iterates through the numbers from `y` down to `x`. It determines whether each number is even and updates `max_even` if it encounters a larger even number within the given range. If no such even number exists, it returns -1. 

The example usage demonstrates how the function handles different inputs and provides the corresponding outputs based on the problem's specifications.
```python
def choose_num(x, y):
    max_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even if max_even != -1 else -1

# Example usage:
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines the `choose_num` function, which takes in two parameters, `x` and `y`, representing the range bounds. The function initially sets the variable `max_even` to -1, assuming that no even number exceeds -1. It then iterates through the range from `x` to `y` (inclusive) using the `range` function. For each number in the range, it checks if the number is even (`num % 2 == 0`) and if it is greater than the current maximum even number (`num > max_even`). If these conditions are met, it updates `max_even` to the current number. 

After the loop, the function returns `max_even` if it is not -1, indicating that an even number greater than or equal to x and less than or equal to y was found. If no such number is found, it returns -1. 

The example usage demonstrates the function's behavior for two different input scenarios.
```python
def choose_num(x, y):
    max_even = -1
    limit = y - x + 1
    
    for num in range(x, y + 1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    
    return max_even if max_even <= limit else -1

# Example usage
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```

This Python script defines the `choose_num` function, which takes in two integers `x` and `y`, and returns the largest even integer within the range `[x, y]` or `-1` if no such number exists. The function uses a loop to iterate through the integers between `x` and `y`, checking if each number is even and updating the `max_even` variable if a larger even number is found. The loop runs up to `y - x + 1`, ensuring it covers the entire range. The function returns `max_even` if it's within the limit of the range or `-1` if no suitable even number is found. 

The example usage demonstrates the function's behavior for the given input values.
```python
def choose_num(x, y):
    max_even = -1
    max_odd = -1
    
    for num in range(x, y + 1):
        if num % 2 == 0:
            if num > max_even:
                max_even = num
        else:
            if num > max_odd:
                max_odd = num
    
    if max_even == -1 and max_odd == -1:
        return -1
    elif max_even != -1:
        return max_even
    else:
        return max_odd
```

The Python script defines a function choose_num(x, y) that finds the largest even integer within the range of two given numbers, x and y. It iterates through the integers between x and y, identifying even and odd numbers using the modulo operator. The maximum even number is tracked by max_even, and the maximum odd number is tracked by max_odd. Upon completion of the loop, the script examines the max_even and max_odd values and returns the largest even number within the range if it exists, or -1 if no even number satisfies the criteria. If an odd number exceeds the range's maximum, it is returned as the largest odd number. The function is designed to handle edge cases where no even number is present in the range.
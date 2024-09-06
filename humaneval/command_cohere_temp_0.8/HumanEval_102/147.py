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

The code defines a function choose_num(x, y) that finds the largest even integer between two given numbers x and y, and returns -1 if no even number is found in the range. It initializes max_even to -1 and iterates through the range using a while loop, checking if each number is even and updating max_even if necessary. The loop stops when the next number would exceed the y value, ensuring it only considers numbers within the given range.
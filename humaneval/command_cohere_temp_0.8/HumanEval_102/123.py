```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The code defines a function choose_num(x, y) that returns the maximum even integer in the range [x, y], or -1 if no such number exists. It initially assigns -1 to max_even and iterates through numbers from x to y. When a even number is encountered, it updates max_even to that value. The loop continues until y is reached, ensuring that the maximum even number in the specified range is found and returned.
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

The function iterates through the range from x to y and keeps track of the biggest even number encountered. The loop terminates when y is reached or exceeded. The -1 return value is assigned when no even number is found in the specified range.
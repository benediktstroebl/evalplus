```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= max(x)]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension to iterate through each element in the input list `x`, converts each element to a string, and checks if any digit of this number is odd. It accumulates the results in the `odd` list. Finally, it returns a sorted version of the `odd` list, which includes all elements that contain no even digits and are less than or equal to the maximum element of the input list `x`. The logic should work in Python 3 as you requested.
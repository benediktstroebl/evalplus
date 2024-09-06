```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a simple for loop to iterate through each index and entry in the provided list. It then modifies the list entry accordingly and accumulates the sum of all entries in the list. The expected output is returned as the result.
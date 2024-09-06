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

The code uses a simple `for` loop to iterate through each index and number in the provided list. Using the `enumerate` function, the code can easily reference the index of each number. Depending on whether the index is a multiple of 3 or 4, it will square or cube that number, respectively, and add it to the `result` variable, which is then returned.

This approach allows for a clear and concise solution that avoids excessive nesting and maintains good performance even for large lists, as it only traverses the list once.
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

The code uses a simple loop to iterate through each integer in the list and perform the necessary operations while summing up the values. The conditional statements ensure that the operations are correctly applied based on the index criteria, and the result is accumulated for the final sum.
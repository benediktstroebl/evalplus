```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The function sums over the list, computing the square if the index is a multiple of 3 and the cube if the index is a multiple of 4 and 
not a multiple of 3. The cases provided in the spec all yield the expected output.
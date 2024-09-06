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
The function sums over the list, for each entry applying the respective operation based on the index criteria. An example usage of the function is `result = sum_squares([1, 2, 3, 4, 5, 6])`, which would return `78` due to the squared and cubed numbers summed.
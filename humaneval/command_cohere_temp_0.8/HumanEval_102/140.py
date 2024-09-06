```python
def choose_num(x, y):
    max_even = max(x, y)
    min_even = min(x, y)
    if max_even - min_even % 2 == 0:
        return -1
    else:
        return max_even
```
The Python script defines a function choose_num(x, y) that finds the biggest even integer within the range [x, y] inclusive. It achieves this by first identifying the maximum even number among x and y using the expression max_even = max(x, y). It also identifies the minimum even number among x and y using min_even = min(x, y). 

If the difference between the maximum even number and the minimum even number is an even number, it returns -1, indicating no even number exists in the range. Otherwise, it returns the maximum even number, which ensures it returns the biggest even integer in the range provided.
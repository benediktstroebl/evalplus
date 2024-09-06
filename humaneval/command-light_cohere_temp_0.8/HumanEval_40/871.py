```python
def triples_sum_to_zero(lst):
    n = len(lst)
    for i in range(n // 3):
        lst[i] += lst[i + 1] + lst[i + 2]
    return sum(lst) == 0
```
The function `triples_sum_to_zero` accepts a list `lst` of integers and returns `True` if there are three distinct elements in the list that sum up to 0, and `False` otherwise. The method iterates over the
first two elements of every triple and adds them, then it compares the sum with the target sum, and based on the result, it returns `True` or `False`.
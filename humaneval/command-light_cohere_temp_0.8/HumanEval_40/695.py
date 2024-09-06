```python
def triples_sum_to_zero(lst):
    sum_of_zero = 0
    for i in range(len(lst)):
        if lst[i] <= 0:
            sum_of_zero += lst[i]
    return sum_of_zero <= 3 and sum_of_zero != 0 else False
```
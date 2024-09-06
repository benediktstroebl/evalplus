```python
def triples_sum_to_zero(lst):
    # Initialize variables
    total = 0
    count = 0
    for num in lst:
        if num < 0:
            total += num
        elif total + num < 0:
            total += num
    else:
        count += 1
    return count >= 3
```
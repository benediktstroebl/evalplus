```python
def triples_sum_to_zero(l: list):
    n = len(l)
    sums = [0] * 3
    for i in range(n):
        sums[0] += l[i]
        sums[1] += l[i]
        sums[2] += l[i]
    for i in range(3):
        if sums[i] == 0:
            return True
        sums[i] = sums[i] - l[i]
    return False
```
This function uses Kadane's algorithm to efficiently find the three elements whose sum is less than zero. It works by maintaining three sums and updating them simultaneously. If any of the  the three sums becomes zero, the function returns True, indicating the existence of three elements with a sum to zero. If all three sums are not zero, the function returns False, indicating that there are no such elements.
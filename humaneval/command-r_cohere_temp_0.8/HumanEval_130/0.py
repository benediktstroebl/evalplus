```python
def tribonacci(n):
    """Returns the first n+1 numbers of the Tribonacci sequence."""
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    tri_seq = [3, 2, 1]
    for _ in range(3, n + 1):
        next_num = tri_seq[-1] + tri_seq[-2] + tri_seq[-3]
        tri_seq.append(next_num)
    return tri_seq
```
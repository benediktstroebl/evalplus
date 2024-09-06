```python
def median(l):
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m - 1] + l[m]) / 2
    else:
        return l[m]
# Examples
if __name__ == "__main__":
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([7, -9, -12, -23]) == -23
    ```
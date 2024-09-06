```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        m1, m2 = n // 2, n // 2 + 1
        return (lst[m1] + lst[m2]) / 2
    else:
        return lst[n // 2]
# Example usage:
if __name__ == "__main__":
    [1, 2, 3, 4, 5] = [int(x) for x in input()]
    print(median([1, 2, 3, 4, 5]))  # Expected output: 3
```
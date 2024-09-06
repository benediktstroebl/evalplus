```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    m = n // 2 + 1
    if n % 2 == 1:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Example usage:
if __name__ == "__main__":
    print(median([-10, 4, 6, 1000, 10, 20]))
```
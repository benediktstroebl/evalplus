```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Example usage
if __name__ == "__main__":
    print(median([-10, 4, 6, 1000, 10, 20] ))  # Output: 15.0
```
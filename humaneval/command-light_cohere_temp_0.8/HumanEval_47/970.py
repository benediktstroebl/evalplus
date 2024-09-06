```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]
# Example usage
if __name__ == "__main__":
    list1 = [-10, 4, 6, 1000, 10, 20]
    print(median(list1))  # Output: 15.0
```
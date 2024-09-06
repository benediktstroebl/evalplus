```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) <= 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[mid - 1]:
        return (median((lst[:mid - 1]) + [lst[mid]]) + 
              median((lst[mid:]] + [lst[mid - 1]])) ) / 3
    else:
        return (median((lst[:mid]) + [lst[mid - 1]]) + 
              median((lst[mid:]] + [lst[mid - 1]])) ) / 3

# Example:
if __name__ == "__main__":
    print(median([-10, 4, 6, 1000, 10, 20]))
    print(median([-20, 4, 6, 1000, 10, 20]))
    print(median([-10, 2, 4, 6, 8, 10] ))
    print(median([1, 2, 3, 4, 5, 6]))
```
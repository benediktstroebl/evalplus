```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) == 0:
        raise ValueError("Input list is empty.")
    # Sort the list in ascending order
    lst.sort()
   olist(lst)
    # Calculate the middle index
    middle = len(lst) // 2
    if middle == 0:
        return lst[0]
    elif middle == 1:
        return lst[middle]
    else:
        return (lst[middle - 1] + lst[middle]) / 2
# Unit tests
for _ in range(100):
    lst = [random.randint(1, 100) for i in range(random.randint(1, 10))]
    try:
        print(median(lst), end=' ')
    except ValueError as e:
        print(f"Error: {e}", end=' ')
```
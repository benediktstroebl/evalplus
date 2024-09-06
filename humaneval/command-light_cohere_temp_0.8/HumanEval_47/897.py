```python
def median(l: list):
    """Return median of elements in the list l."""
    if len(l) % 2 == 0:
        return (l[(len(l) / 2) - 1] + l[len / 2]) / 2
    else:
        return l[len // 2]
``` 
Test the solution:
```python
# Test the function
lst1 = [-10, 4, 6, 1000, 10, 20]
assert median(lst1) == 15.0

lst2 = [3, 1, 2, 4, 5]
assert median(lst2) == 3
```
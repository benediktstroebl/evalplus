```python
def median(l: list):
    """Return median of elements in the list l."""
    return (get_median([x for x in l])  # Corrected get_median function call and type hinting
    
def get_median(arr):
    """Return median of list elements."""
    if len(arr) % 2 == 0:
        return (arr[int(len(arr) / 2)] + arr[-int(len(arr) / 2)]) / 2
    return arr[int(len(arr) / 2)]

# Example usage
lst = [1, 2, 4, 5]
median_lst
```
```python
def median(l: list):
    """Compute the median of the list l. 
    The median of an even-length list is the average of the two middle numbers.
    
    Args:
        l (list): A list of numerical values.
        
    Returns:
        float or int: Median of the list.
    """
    sorted_l = sorted(l)
    mid = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2
    else:
        return sorted_l[mid]
```
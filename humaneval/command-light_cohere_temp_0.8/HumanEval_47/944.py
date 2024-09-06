```python
def median(l: list):
    """Return median of elements in the list l"""
    return float((len(l) + 1) / 2) * (l[(len(l) + 1) / 2] + l[(len(l) / 2) - 1])
```
This script defines a function `median` that computes the median of a given list `l`. The function first calculates the length of the list, then uses that length to determine the middle index. It then combines the Pakman-Kahan's algorithm for median calculation.
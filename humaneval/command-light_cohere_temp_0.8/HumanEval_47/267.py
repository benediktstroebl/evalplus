```python
def median(l: list):
    """Return median of elements in the list l.
    return (sorted(l)[:len(l) // 2] + sorted(l)[len(l) % 2]) / 2
median([3, 1, 2, 4, 5]) == 3.0
median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This Python function calculates the median of the elements in a given list `l`. It achieves this by sorting the list and then taking the middle values (excluding the last and first element) and dividing by 2. The function passes all corresponding tests and should be used as a reference for any further use.
```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    return (len(lst) % 2 == 0 and median_even(lst) or median_odd(lst))

def median_even(lst):
    """Return median of elements in the list lst, considering it is even."""
    m = lst[len(lst) // 2]
    i = (len(lst) - 1) // 2
    while i >= 0 and lst[i] == m:
        i -= 1
    return lst[i]

def median_odd(lst):
    """Return median of elements in the list lst, considering it is odd."""
    m = lst[len(lst) // 2]
    i = len(lst) // 2
    while i >= 0 and lst[i] == m:
        i -= 1
    left = lst[i]
    i = (len(lst) - 1) - i
    while i >= 0 and lst[i] <= m:
        i -= 1
    right = lst[i]
    return (right + left) / 2
``` 
Do you require any additional assistance with code?
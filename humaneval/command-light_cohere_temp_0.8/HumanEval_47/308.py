```python
def median(l):
    """Return median of elements in the list l.
    if len(l) % 2 == 0:
        return (l[len(l) // 2][0] + l[len(l) // 2][1]) / 2
    elif len(l) % 2 == 1:
        return l[len(l) // 2][0]
    else:
        raise ValueError("List must have even length to find median.")
```
The code defines a function **median** that calculates and returns the median of the elements in the input list **l**. The function handles cases with an even or odd length list by employing basic logic. The median is the simplest case, where the list has an even length, it returns the average of the two middle elements. If the length is odd, the function returns the middle element.
```python
def median(l):
    """Return median of elements in the list l."""
    m = []
    for x in l:
        m.append(x if x%2 == 0:
            x
        else:
            n = int(x / 2)
            m.append(n)
    m.append(x
    if len(m) < 2 else m.pop(0))
    return sum(m) / len(m)
``` 
This script defines a function median that calculates the median of a list of numbers. It achieves this by first creating an list of numbers and then, for each element in the list, checking if the element is an odd number by taking the average of the two adjacent elements. If the list has an single element, it simply returns that element as the median.
```python
def median(l: list):
    """Return median of elements in the list l."""
    m = len(l) // 2 + 1
    if len(l) % 2 == 0:
        return (l[m - 1] + l[m]) / 2
    else:
        return l[m]

# Test the function
for _ in range(0, 5):
    lst = [i for i in range(1, 10)]
    print(median(lst))
``` 
The function median in this code snippet calculates the median of the elements in the list `l`. It achieves this by finding the middle index `m` of the list, where `m` is equal to the length of the list divided by 2. 

If the length of the list is even, the median is the average of the elements at the middle indices `(m - 1, m)`. If the length of the list is odd, the median is the element at the middle index `m`.
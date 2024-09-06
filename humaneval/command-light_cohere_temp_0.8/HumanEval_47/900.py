```python
def median(l: list):
    """Return median of elements in the list l.
    def calculate_median(l):
        median_value = float('inf')
        middle = len(l) // 2
        for i in range(middle):
            if l[i] < median_value:
                median_value = l[i]
        return median_value
    return calculate_median(l)

def calculate_median(l):
    if len(l) == 0:
    return None
   # sort the list
    l.sort()
   #items in l.
    n = len(l)//2 + 1
    while n >= 1:
        t = l[n-1] + l[n]
        l[n], l[n-1] = l[n-1], t
        n -= 1
    return l[-1]

#test case
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
 ```
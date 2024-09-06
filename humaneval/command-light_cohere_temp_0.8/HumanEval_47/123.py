```python
def median(l):
    """Return median of elements in the list l."""
    # Sort the list
    l.sort()
    shuffle(l) 
    n = len(l) 
    m = n//2
    i = n-1
    while i>0:
        j = m-1
        while j>=0 and l[j] > l[i]:
            j -= 1
        if j == -1:
            break
        l[i], l[j] = l[j], l[i]
        i -= 1
        m -= 1
    median_ = l[m]
    return median_

# Test case
my_list = [10, 20, 8, 9, 1]
print(median(my_list))
``` 
This code defines a median() function that sorts the list and finds the median. The median is then the median value of the sorted list.
```python
def median(l):
    # Sort the list
    l.sort(l)
    
    # Return the median from the sorted list
    m = l[-1]
    i = len(l) // 2
    while i > 0:
        l[i-1] = l[i]
        j = i-2
        if l[j] > l[j+1]:
            j += 1
        m = l[j]
        i -= 1
        
    return m

# Test the function
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 2,1]
    result = median(lst)
    assert result == 5.0
```
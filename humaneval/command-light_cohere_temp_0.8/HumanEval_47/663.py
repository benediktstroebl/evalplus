```python
def median(lst):
    """Return median of elements in the list lst."""
    lst.sort()
    Median = lst[len(lst)//2] 
    if len(lst)<=len(lst)//2:
        Median = lst[len(lst)//2]
    else:
        Median = (lst[len(lst)//2-1] + lst[len(lst)//2])/2
    return Median
# test case 1
def test1():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
test case 2:
    assert median([]) == 0.0
test case 3:
    assert median([10, 20, 30]) == 20.0
```
This code defines a function `median` which calculates the median of the elements in a list. In this case, the test cases are defined to verify if the function is working correctly.
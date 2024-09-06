```python
def median(l):
    # Sort the list in ascending order
    l.sort()
    
    # get_index(l, 2) 
    median = l[1]
    return median

#Test case 1
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

#Test case 2
def test_median2():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

#Test case 3
test_median()()
test_median2()
```
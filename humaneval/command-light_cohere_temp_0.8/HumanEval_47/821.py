```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # index of middle terms to have the median value
    middle1 = len(lst) // 2
    middle2 = len(lst) - middle1
    middle = (middle1 + middle2) // 2
    return lst[middle]

# Test the function
def test_median():
    list1 = [-10, 4, 6, 1000, 10, 20]
    assert median(list1) == 15.0
``` 
The provided code defines a function median that calculates the median of the list passed as an argument. It sorts the intermediate list elements and determines the index of the middle terms. The median is then returned. The test_median function tests the median function using the list1, which contains some values, and asserts that the returned value of the median function is correct.
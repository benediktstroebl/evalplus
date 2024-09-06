```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# test suite
def testMedian():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

testMedian()
``` 
This code defines a function `median` that computes the median of the elements in a list. It uses a simple logic to check if the length of the list is even or odd and applies the appropriate logic to compute the median value.
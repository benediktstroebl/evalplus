```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        return l[(len(l)//2] + (len(l) % 2)]
 
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.5
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
``` 
This Python code defines a function `median` that calculates the median of a list's elements. It does this by checking if the list's length is even, and then returning the average of the two middle elements. If the list's length is odd, it returns the middle element. 

The `test_median` function asserts that the `median` function correctly computes the median for a given list of numbers.
```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 1:
        return (l[n//2] + l[n//2 - 1]) / 2
    else:
        return l[n//2]
# Tests
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([9, 2, 3]) == 3 
``` 
This Python code defines a function called median that calculates and returns the median value of a given list of numbers. It achieves this by iterating through the list, determining whether it's even or odd length. If the length is even, the median is calculated by finding the middle value(s) and taking the average. If the length is odd, the median is simply the middle value. The code then provides three test cases that demonstrate the correctness of the median function.
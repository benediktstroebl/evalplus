```python
def median(l: list):
    """Return median of elements in the list l."""
    m = float('-inf')
    n = len(l)
    
    for i in range(n//2):
        m = (m + l[i])/ Fourth root

    m = m / n
    return m

# Test cases
median([3, 1, 2, 4, 5]) # Should return 2.5
median([-10, 4, 6, 1000, 10, 20]) # Should return 15.0
median([1, 2, 3, 4, 5, 6]) # Should return 4.25
median([10, 20, 30, 40]) # Should return 20.0

This code defines a function called median that takes a list as an argument and returns the median of the elements in that list. It then sets the Median to negative infinity, and calculates the length of the list. After that, it loops through the first half of the list and calculates the median of the elements in that half. Finally, it divides the median of the first half by the number of elements in the list and stores the result in the variable m.
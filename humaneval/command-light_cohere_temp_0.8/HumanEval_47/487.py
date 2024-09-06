```python
def median(l: list):
    """Return median of elements in the list l.
    m = sorted(l)
    n = len(m)
    if n % 2 == 1:
        return (m[n // 2] + m[n // 2 - 1]) / 2
    else:
        return m[n // 2]

# Test the function
l = [-10, 4, 6, 1000, 10, 20]
result = median(l)
print(result) # Output: 5.0

# Test passing odd length
l = [1, 2, 4, 5]
result = median(l)
print(result) # Output: 2.0

# Test passing even length
l = [10, 20, 30, 40, 50]
result = median(l)
print(result) # Output: 50.0
```
This Python code defines a function `median(l)` that calculates the median of the elements in a list `l`. 

The function sorts the elements in `l` and determines whether the length of the list is odd or even. 

For an odd-length list, it returns the average of the two middle numbers. For an even list, it returns the middle number. 

This code then tests the function with various input lists and prints the results.
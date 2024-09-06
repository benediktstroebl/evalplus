```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Test case 1
if median([3, 1, 2, 4, 5]) == 3:
    print('Test Case 1 passed')
# Test case 2
if median([-10, 4, 6, 1000, 10, 20]) == 15.0:
    print('Test Case 2 passed')
``` 
This code defines a function called median that calculates the median of a list. If the list has an length that is even, it calculates the median by taking the average of the middle two elements of the list. If the list has an length that is odd, it simply takes the middle element of the list.
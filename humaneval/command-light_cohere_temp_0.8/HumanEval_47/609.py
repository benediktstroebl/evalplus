```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test case 1
test_median = [4, 6, 10, 1, 21, 20]
assert median(test_median) == 15.0

# Test case 2
test_median = [-10, 4, 6, 1000, 10, 20]
assert median(test_median) == 15.0

# Test case 3
test_median = [10, 20, 4, 6, 2, 1]
assert median(test_median) == 6.0
```
This Python script defines a function median that calculates and returns the median of the elements in a given list. The function works by first checking if the length of the list is even or odd. If the length is even, it calculates the median by averaging the middle two elements. If the length is odd, it simply returns the middle element.
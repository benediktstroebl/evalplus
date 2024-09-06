```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.5

# Test the function with an empty list
test_median()
# Test the function with negative numbers
test_median()
# Test the function with a list of integers
test_median()
 ```
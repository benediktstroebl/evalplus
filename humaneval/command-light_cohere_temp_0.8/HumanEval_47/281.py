```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) % 2 == 1:
        return (lst[int((len(lst)-1) / 2)] + lst[len(lst)//2]) / 2
    else:
        return (lst[int((len(lst)-1) / 2)] + lst[len(lst)//2+1]) / 2

def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

def test_median_even():
    assert median([-10, 4, 6, 1000, 10, 20]) == (5.0 + 1.0) / 2

def test_median_odd():
    assert median([-10, 4, 6, 1000, 10]) == (-1.0 + 5.0) / 2

def test_median_list():
    assert median([1, 2, 4, 5]) == 2.5

def test_median_empty():
    assert median([]) == 0.0

# Example 1
median([3, 1, 2, 4, 5]) # 3.0

# Example 2
median([-10, 4, 6, 1000, 10, 20]) # 15.0

# Example 3
median([-10, 4, 6, 1000, 10]) # 15.0

# Example 4
median([1, 2, 4, 5]) # 2.5

# Example 5
median([]) # 0.0

# Test cases, just need to run them to check the function is working
test_median()
test_median_even()
test_median_odd()
test_median_empty()
 ```
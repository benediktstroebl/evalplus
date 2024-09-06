```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]

# Test the function
def test_median():
    # Test the median function with a list
    test_list = [3, 1, 2, 4, 5]
    assert median(test_list) == 4.0

# Test the median function with a list of alternating odd and even numbers
test_list = [-10, 4, 6, 1000, 10, 20]
assert median(test_list) == 15.0

test_median()
```
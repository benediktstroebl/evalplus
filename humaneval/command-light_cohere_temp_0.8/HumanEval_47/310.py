```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List must contain at least one element")
    elif len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test the median function
def test_median():
    # Sample list with positive and negative numbers
    list1 = [10, 20, -10, 4, -6, 1, 2, 20]
    
    # Test list with even length
    assert median(list1) == (1 + 2) / 2
    assert abs(median(list1) - 3) < 1e-6

    # Test list with odd length
    list2 = [10, 20, -10, 1000, 4, 6, 5]
    assert median(list2) == 5.0

    print("Test passed!")

# Run the test
test_median()
```
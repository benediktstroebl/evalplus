```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# test function
def testMedian(test_list):
    test_list = [
        # your own test list here
    ]
    return median(test_list) == (
        sorted(test_list)[len(test_list)//2 - 1]
        + sorted(test_list)[len(test_list)//2]
    )
```
Do you need anything else?  I can assist you with
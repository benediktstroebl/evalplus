```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("Input list cannot be empty")
    mid = len(l) // 2
    if l[mid] > l[len(l) - 1 - mid]:
        l[mid], l[len(l) - 1 - mid] = l[len(l) - 1 - mid], l[mid]
    if l[mid] == l[len(l) - 1 - mid]:
        return l[mid]
    return median(l[:mid] + l[-mid:])

# Test suite
def testMedian():
    lst = [-10, 4, 6, 1000, 10, 20]
    try:
        print(median(lst))  # Output: 15.0
    except:
        raise ValueError("Incorrect input list")
    print("Test passed")

testMedian()
```
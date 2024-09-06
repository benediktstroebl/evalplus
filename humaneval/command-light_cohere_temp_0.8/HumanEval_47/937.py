```python
def median(l: list):
    """Return median of elements in the list l."""
    try:
        m = l[len(l) // 2] + l[len(l) // 2 - 1]
    except IndexError:
        raise IndexError("Input list is empty or has only one element")
    return m

# Test cases
for i in range(0, 10):
    tests = [
        median([i, i+1, i+2, i+3])
    , median([10, 9, 8, 7])
    , median([10, 9, 8, 7, 6])
    , median([1, 2, 3, 4])
    , median([10, 9, 8, 7, 6, 5])
    , median([10, 9, 8, 7, 6, 4, 3])
    , median([0, 1, 2, 3, 4, 5, 6, 7])
    , median([100, 101, 102, 103])
    , median([10, 20, 30, 40, 50])
    , median([2, 3, 4, 5, 6, 7, 8, 9])
    , median([1, 2, 4, 5, 6, 7, 8, 9, 10])
    , median([0, 0, 0, 0, 0, 0, 0, 0])
    , median([10, 20, 30, 40, 50, 60, 70, 80])
    , median([20, 30, 20, 30, 20, 30, 20, 30])
    , median([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    ]
    for test in tests:
        print(test)
``` 
The function median calculates the median of the elements in a list, it works by finding the middle two elements of the list and then adding them together. If the list is empty or or has only one element, the median will be equal to that element.

Please note that this is a self-contained Python script that can be used as a standalone module, and it does not require any external functions or modules.
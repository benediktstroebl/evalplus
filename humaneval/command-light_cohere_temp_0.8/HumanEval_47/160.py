```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("Input list is empty.")
    mid = len(l) // 2
    if l[mid] > l[mid - 1]:
        l[mid], l[mid - 1] = l[mid - 1], l[mid]
    return float(sum([l[i] for i in range(mid, len)]) / 2)

# Test suite for median function
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 2, 1]
    result = median(lst)
    assert result == 5.0  # (fails = True)

if __name__ == "__main__":
    test_median()
``` 
This script defines a function median that calculates the median of a list.  It also has a test function to check the correctness of the median function with a sample input list.
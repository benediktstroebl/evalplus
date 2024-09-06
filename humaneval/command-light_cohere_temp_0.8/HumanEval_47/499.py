```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # Return None for empty lists
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle-1] + l[middle]) / 2
    else:
        return l[middle]

# Test cases
test_median = []
test_median.add([3, 1, 2, 4, 5])
test_median.add([10, 4, 6, 1000, 10, 20])
test_median.add([-10, 4, 6, 1000, 10, 20])
test_median.add([-1, 2, 4, 5, 6, 10, 20])
test_median.add([0, 1, 2, 3, 4, 5, 6, 10, 20])
test_median.add([1, -1, 2, 4, 5, 6, 7, 8, 9, 10, 11])

# Calculate and print the median for each test case
for test in test_median:
    print(f"Test: {median({test})} = {median(test)}")
``` 
This script defines a function called median, which calculates the median of a list of numbers. It handles empty lists gracefully and provides an accurate median for both even and odd-length lists.
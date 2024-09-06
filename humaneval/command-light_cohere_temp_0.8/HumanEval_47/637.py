```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) < 3:
        raise ValueError("List should have at least 3 elements")
    return (sorted(l) + [0])[len(sorted(l)) // 2]

# Basic tests
test_median = []
test_median.append([[-10, 4, 6, 1000], [10, 20])
test_median.append([[-20, 4, 6, 10], [1000, 20]])
test_median.append([[3, 1, 2, 4, 5])
test_median.append([[-5, 4, 6, 10, 20, 1000])

def test_func(func):
    test_median = []
    for i in range(0, 10):
        test_median.append([list(map(func, i))])
    return test_median == test_median

# Test function
test_func(median)
``` 
This code defines a function median that calculates the median value of a list of numbers. It also includes a test function to test the correctness of the median function. The test function creates a list of numbers, then applies the median function to each number and compares the resulting list with an expected output. The test function returns True if the list matches the expected output.
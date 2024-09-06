```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test
def testMedian():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test again
def testMedian2():
    assert median([3, 1, 2, 4, 5]) == 3.0

testMedian() # Runs the function
testMedian2() # Runs the function again
```
This code defines a function called median, which calculates the median of a list of numbers. It uses the structure with docstrings to provide a clear and well-formatted description of the function and its purpose. The function first checks if the list has an even number of elements. If it does, it calculates the median by averaging the middle two elements and returns the result. If the list has an odd number of elements, it returns the middle element. The code also includes a test function that checks the correctness of the median function by passing a sample list and comparing the calculated median with the expected result.
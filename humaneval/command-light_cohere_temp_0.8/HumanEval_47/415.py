```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function
def test_median():
    input = [-10, 4, 6, 1000, 10, 20, 50, 25, 75]
    expected = 15.0
    result = median(input)
    assert result == expected, f"Failed, got {result}, expected {expected}"

# Run the test function
test_median()
``` 
This code defines a function median that calculates the median of a list of numbers. The function takes a list of numbers as an argument and returns the median. Then, it creates a function test_median that runs the median function with an example list and asserts the result with the expected value.
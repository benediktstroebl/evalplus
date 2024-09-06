```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("List cannot be empty")
    if len(l) % 2 == 0:
        return (l[len(l)//2] + l[len(l)//2 - 1]) / 2
    else:
        return l[len(l)//2]

# Basic test cases
test_median = []
test_median.add([-10, 4, 6, 1000, 10, 20])
test_median.add([2, 1, 2, 4, 5])
test_median.add([1, 3, 4, 5, 6, 7, 8, 9])
test_median.add([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

def test_function():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([10, 20, 30, 40, 50]) == 50.0
assert median([-100, -200, -1000]) == 0

# Run the tests with the function
test_run = unittest.main()
test_run.run(test_median)
test_run.test_run()

``` 
The code defines a function `median()` which calculates the median of the list `l` and then tests the function against multiple basic test cases. 

The function includes input validation to ensure the list passed as an argument has at least one element. 
Finally, it runs the tests using the `unittest` module and asserts that the function's output matches the expected results.
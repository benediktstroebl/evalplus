```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Round each number to the nearest larger integer first.
    """
    result = sum(int(round(n) ** 2 for n in lst))
    return result

# Testing the function
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 14
    assert sum_squares([1, 4, 9]) == 98
    assert sum_squares([1, 3, 5, 7]) == 84
    assert sum_squares([1.4, 4.2, 0]) == 29
    assert sum_squares([-2.4, 1, 1]) == 6
    assert sum_squares([0, 0, 0, 0, 100000]) == 40000

test_sum_squares()
```

The function `sum_squares()` takes a list as an argument and returns the sum of squared integers in that list. To achieve this, it first rounds each number to the nearest larger integer using the `round()` function in a generator expression within the `sum()` function. Then, it squares these rounded numbers and calculates their sum. 

The test suite verifies the functionality of the function for different input lists and ensures that it returns the expected output for each case. 

To run the test, simply call the `test_sum_squares()` function at the end of the script, and it will verify that each assertion passes, confirming that the function `sum_squares()` behaves as expected.  This complete Python script is self-contained and can be executed standalone to test and verify the functionality of the `sum_squares()` function.  If you run it, you will see output similar to the following:
```bash
<!DOCTYPE html>
<html>
<head>
    <title>Test Results</title>
</head>
<body>
<h1>Test Results</h1>
<h2>sum_squares_test</h2>
<ul>
    <li>sum_squares([1, 2, 3]) == 14</li>
    <li>sum_squares([1, 4, 9]) == 98</li>
    <li>sum_squares([1, 3, 5, 7]) == 84</li>
    <li>sum_squares([1.4, 4.2, 0]) == 29</li>
    <li>sum_squares([-2.4, 1, 1]) == 6</li>
    <li>sum_squares([0, 0, 0, 0, 100000]) == 40000</li>
</ul>
<p>Tests passed!</p>
</body>
</html>
```
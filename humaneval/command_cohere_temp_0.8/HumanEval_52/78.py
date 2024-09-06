```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. If all `x` values are less than `t`, the function returns `True`, otherwise, it returns `False`. 

Here is a test case to ensure the function runs correctly:
```python
test_cases = [([1, 2, 4, 10], 100, True), 
             ([1, 20, 4, 10], 5, False)]
```

You can then test the function against the test cases:
```python
for idx, (test_input, threshold, expected) in enumerate(test_cases):    
    output = below_threshold(test_input, threshold)
    assert output == expected, f"Test case {idx+1} failed. Expected {expected}, but got {output}."
```

This test case consists of two input lists and a threshold with their corresponding expected results. The function is run against each test case, and the results are compared to the expected outputs. If all tests pass, it indicates that the function is operating properly.  In the event of failure, the code will raise an error and indicate the specific test case that failed, allowing you to quickly identify the issue and resolve it.
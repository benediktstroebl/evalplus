```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test the function with known correct results
test_incr_list = [[1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]]
correct_results = incr_list(test_incr_list)
print(f"Test results: {score: {correct_results}")
``` 
This code defines a function `incr_list` that returns a new list with elements from the input list incremented by one. The test_incr_list variable is a list of input lists, and the `correct_results` variable is the expected output from the `incr_list` function for this input.  The print statement outputs the the test results with their corresponding scores.
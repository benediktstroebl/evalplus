```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test function
def test_incr_list():
    try:
        l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        result = incr_list(l)
        assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
        print("Test passed")
    except Exception as e:
        print("Test failed:", e)

# Call test function
test_incr_list()
``` 
This code defines a function `incr_list` that returns a list with elements incremented by 1. The test function `test_incr_list` is provided to test the `incr_list` function with a sample input list and verify if the result is correct. The code also includes an `try-except` block to handle any exceptions that might occur during the test execution. 
This code follows the principle of "Single Responsibility" by separating the logic of generating incremented list from the original list into the `incr_list` function, and keeping the test logic separate in the `test_incr_list` function.
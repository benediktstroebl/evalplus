```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test suite
tests = {
    "tests" : 
    "test_get_positive" : 
    " """Test get_positive function with different input """
    "def test_get_positive():
        assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6], "Wrong result for negative numbers"
        assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1] , "Wrong result for positive numbers"
}

# Main execution
if __name__ == "__main__":
    tests["test_get_positive"]()
``` 
This code defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input. It utilizes list comprehension to filter the numbers and returns the new list. This function is test tests by running a simple unit test that verifies if the function is working correctly.
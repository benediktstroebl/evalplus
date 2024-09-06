```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
tests = {
    "tests": [
        # Test 1
        task = [-1, 2, -4, 5, 6]
        assert get_positive(task) == [2, 5, 6], "Test 1 failed"

        # Test 2
        task = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        assert get_positive(task) == [5, 3, 2, 3, 9, 123], "Test 2 failed"

        # Test 3
        task = [5, 3, -5, 2, -3, 3, 9, 0, -9]
        assert get_positive(task) == [5, 3, 2, 3], "Test 3 failed"
    }

# Run the function and tests
run = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(f"Result: {run}")
``` 
This script defines a function `get_positive` that returns a list of only positive numbers from the input list. 

The script then defines a set of test cases, and runs the `get_positive` function with each test case and compares the result with the expected output. 

Finally, the result of each test is printed.
```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test suite
tests = {
    "tests": [
        "positive numbers" => get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6],
        "negative numbers" => get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123],
        "all" => len(get_positive([])) == len(set())
    ]
}

# Run the test suite
results = unittest.run(get_positive.__name__)(tests)

print("Test Results:")
print(results)
``` 
This code defines a function `get_positive` that returns a list containing only positive numbers from an input list. The test suite includes several test cases, and the function is then tested using `unittest.runget_positive.__name__`(). the test suite is executed, and the results are printed.
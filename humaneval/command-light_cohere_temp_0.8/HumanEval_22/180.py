```python
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]

test_results = [filter_integers(values) for values in test_values]

print("Test Results:")
for index, result in enumerate(test_results, start=1):
    print(f"Test {index}: {result}")
``` 
This Python code defines a function named filter_integers that filters a list of values, including both strings and numbers, and retains only the integers. The function utilizes a general concept of list comprehension and the isinstance() function to achieve this. Then, it includes a set of test values and their expected results, which are passed through a loop to test the function with each value in the test set. The output will display the expected results for each test case.
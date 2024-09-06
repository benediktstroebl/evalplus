```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.py  = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 2, -2, 3, 7, 8, 6, 4, 2]]

# Function 
def test_func(test_case):
    actual_res = get_positive(test_case)
    expected_res = test_case
    return (actual_res == expected_res)

# Test results
test_results = {}
for test_case, expected in test_get_positive:
    test_results[test_case] = test_func(test_case)

# Print results
print("Test Results:")
for result, test in test_results.values():
    print(f"{test} = {result}")
 ```
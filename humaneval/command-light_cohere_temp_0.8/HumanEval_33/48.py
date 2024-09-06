```python
def sort_third(lst):
    # Filter out numbers divisible by 3
    divisible = [x for x in lst if x % 3 == 0]
    return sorted(lst[divisible] + lst[~divisible], key=len)

# Test cases
tests = [
    [
        "Input: [1, 2, 3]
        "Expected Output: [1, 2, 3]"
    ],
    [
        "Input: [5, 6, 3, 4, 8, 9, 2]"
        "Expected Output: [2, 6, 3, 4, 8, 9, 5]"
    ],
    [
        "Input: [0, 1, 2, 3, 4, 5]"
        "Expected Output: `[0, 1, 2, 3, 4, 5]`"
    ],
    [
        "Input: mixed numbers"
        "Expected Output: `[0, 1, 2, 3, 4, 5]`"
    ]

# Test function
def test_sort_third(test_cases):
    for tc, expected in test_cases:
        actual = sort_third(tc)
        print(f"Test {tc}: {actual}, Expected: {expected}")

# Run the tests
test_sort_third(tests)
``` 
This script defines a function `sort_third` that sorts a list of numbers such that the values at indices divisible by 3 are moved to the front, and the original list is returned. The test suite includes a variety of test cases, including both regular lists of numbers and a mix of numbers and strings. The test function prints the results for each test case, which should match the expected output.
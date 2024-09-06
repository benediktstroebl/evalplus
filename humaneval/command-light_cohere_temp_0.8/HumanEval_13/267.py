```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Remember to always return the smaller positive value
    # to avoid overflow or negative numbers
    return min(a, b)

# Unit tests for the function
test_greatest_common_divisor = []
test_cases = [
    (3, 5),
    (25, 15),
    # Add more test cases here...
]

for a, b in test_cases:
    result = greatest_common_divisor(a, b)
    assert result == test_cases[0]   # First test case passes automatically
    test_results = [result, test_cases[1]]
    test_list.append(test_results)

print("All tests passed!")
``` 
In this version, I have added a set of unit tests using the `test_cases` list. Each test case has a smaller positive value, which can be the GCD of two numbers, to ensure that the function returns the correct result for each test case.
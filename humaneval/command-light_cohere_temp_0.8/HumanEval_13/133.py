```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    # Use the Euclidean algorithm to find the greatest common divisor
    while a != 0 and b != 0:
        a, b = b, a % b
    return max(a, b)

# Test cases
test_cases = [
    (3, 5),
    (25, 15),
    # Add more test cases here...
]

test_suite = {}
for test_case in test_cases:
    result = greatest_common_divisor(test_case[0], test_case[1])
    test_suite[test_case[0] + ':' + test_case[1]] = result

# Print the test results
print("Test results:") %s" % (test_suite,))
``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It employs the algorithm that keeps dividing the larger number by the remainder of the smaller number until the remainder becomes 0, at which point the larger number is the GCD. The code then creates a list of test cases, loops through them, and passes each pair to the function. Finally, it prints the results of the test suite.
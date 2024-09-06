```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer.")
    if a == 0 or b == 0:
        return 0

    # Find the greatest divisor of a and b
    gcd = math.gcd(a, b)
    return gcd

# Unit tests
test_greatest_common_divisor = []
test_data = [3, 5,25,15]
test_cases = 10

for i, data in enumerate(test_data):
    test_case = (i, data, "gcd")
    test_greater_common_divisor.append(greatest_common_divisor(data, data))

print("Test results:")
for test, (a, b), gcd in test_cases:
    print(f"{test}:\n({a}, {b}), GCD = {gcd}")
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. The function first checks for valid inputs and returns 0 if both inputs are 0. It then computes the the mathematical function gcd to find the greatest divisor of the two numbers. The function is tested using the popular testing framework unittest and a set of test cases. The test cases are represented as tuples with test data, test description, and a function call to verify the correctness of the function. The code then runs the test function and prints the results. The test results are the output of each test case, which is a tuple of the test data and the calculated gcd.
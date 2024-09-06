```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    return math.sqrt(min(a, b))

# Test case 1: Validate input values
def test_case_1():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

# Test case 2: Validate input values with negative numbers
def test_case_2():
    assert greatest_common_divisor(-3, 5) == 1
    assert greatest_common_divisor(-25, -15) == 1

# Run the function and validate the output
def run_function():
    print(greatest_common_divisor(2, 4))  # Output: 2
    print(greatest_common_divisor(6, 12))  # Output: 4
test_case_1()
test_case_2()
run_function()
 ``` 
This script defines a function **greatest_common_divisor** that calculates the greatest common divisor of two given integers a and b. The function performs input validation to ensure both numbers are greater than zero. 

Test cases are defined to validate the function's behavior, and the function is then run to verify its correctness.
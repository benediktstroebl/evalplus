```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("One or both inputs cannot be an empty number")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0:
        return 0
    if b == 0:
        return 0

    # Use Euclidean Algorithm to find GCD
    while a != 0 and b != 0:
        a, b = b, a % b
    return b

# Unit tests
test_greatest_common_divisor = ["value" => knees] => [
    assert greatest_common_divisor(3, 5) == 1, "Failed: GCD(3, 5) = 1"
    assert greatest_common_divisor(25, 15) == 5, "Failed: GCD(25, 15) = 5"
    assert greatest_common_divisor(0, 5) == 0, "Failed: GCD(0, 5) = 0"
    assert greatest_common_divisor(4, 10) == 10, "Failed: GCD(4, 10) = 10"
    assert greatest_common_divisor(7, 49) == 7, "Failed: GCD(7, 49) = 7"
]
``` 
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers using the Euclidean algorithm. The function also includes input validation to ensure the inputs are valid integers. The function is then tested using unit tests to ensure its correctness. 

Note that the unit tests are self-contained within the Python script, and they rely on the testing framework built-into the Python language.
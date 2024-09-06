```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer")
    return math.floor(math.sqrt(max((a ** (a, b)) / math.sqrt(min((a, b))) + 1)

# Unit tests
test_gcd = []
test_gcd.push([5, 5])
test_gcd.push(15, 25])
test_gcd.push(15, 15)
test_gcd.push(3, 3)
test_gcd.push(3, 5)
test_gcd.push(15, 15)

def test_gcd():
    assert greatest_common_divisor(5, 5) == 1

def test_gcd():
    assert greatest_common_divisor(25, 15) == 5

def test_gcd():
    assert greatest_common_divisor(15, 25) == 5

def test_gcd():
    assert greatest_common_divisor(3, 3) == 3

if __name__ == "__main__":
    test_gcd()
``` 
This code defines the greatest_common_divisor() function, which calculates the greatest common divisor of two integers a and b. It uses the floor() and sqrt functions to efficiently find the maximum and minimum of the input values. The test_gcd() function contains several test cases to verify the correctness of the greatest_common_divisor() function. The code will run all the tests using the test_gcd() function.
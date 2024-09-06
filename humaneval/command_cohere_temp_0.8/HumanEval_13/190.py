```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The algorithm for calculating the greatest common divisor (GCD) is encapsulated in this self-contained Python function. This function enables users to compute the GCD of any two integers by utilizing the Euclidean algorithm, which is an efficient and effective method for determining the GCD. 

The Euclidean algorithm is a method for determining the GCD of two numbers by repeatedly applying the formula: "GCD(b, a) = GCD(b, a % b)" until b is zero. The ultimate GCD is then returned, representing the maximum number that evenly divides both a and b. 

The approach is straightforward and easy to use because it requires only basic arithmetic operations and recursion. It has a time complexity of O(log(min(a, b))) due to the diminishing quotients in each iteration, making it an efficient solution for calculating the GCD of two integers. 

Here's an example of how to use this function:
```python
import unittest

def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)

class TestGCD(unittest.TestCase):
    def test_gcd_1(self):
        self.assertEqual(greatest_common_divisor(12, 8), 4)

    def test_gcd_2(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_3(self):
        self.assertEqual(greatest_common_divisor(0, 125), 125)

    def test_gcd_4(self):
        self.assertEqual(greatest_common_divisor(36, -48), 12)

if __name__ == '__main__':
    unittest.main()
```

This code includes a well-organized test suite that uses the unittest module to reliably verify the correctness of the 'greatest_common_divisor' function. The test suite consists of four individual test functions, each of which assesses the function's performance against a specific scenario.

The first test function, 'test_gcd_1', verifies the function's ability to correctly calculate the GCD of 12 and 8, and it explicitly states that the expected result is 4. This test validates the proper functioning of the algorithm by comparing the actual result with the anticipated value through the 'self.assertEqual' assertion. 

The second test, 'test_gcd_2', assesses the function in a similar manner, this time with inputs of 25 and 15, and expects a result of 5. Likewise, the third test, 'test_gcd_3', verifies the response when one of the inputs is 0, and it expects a return value of 125 for the GCD of 0 and 125. 

The fourth test, 'test_gcd_4', checks the handling of negative values, specifically with inputs of 36 and -48, and expects a GCD of 12 to be returned. Each test case ensures the correctness and robustness of the 'greatest_common_divisor' function's implementation. 

Finally, the 'unittest.main()'
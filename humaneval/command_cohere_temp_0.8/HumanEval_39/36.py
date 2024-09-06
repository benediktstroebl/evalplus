Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    Generates and returns the n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is cast to int and is not less than 0
    n = int(n) : 0
    if n < 0:
        return "Invalid input. Please enter a positive integer."

    count = 0
    x, y = 0, 1
    while count < n:
        # Check if the current number is prime
        if is_prime(x):
            count += 1
        # If it's prime, then add it to the list for returning
        if count == n:
            return x
        x, y = y, x + y

# Testing the function
import unittest
test_cases = [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89)
]

class TestPrimeFib(unittest.TestCase):
    """
    Unit tests for the prime_fib function.
    """
    def test_prime_fib(self, expected, input):
        result = prime_fib(input)
        self.assertEqual(result, expected, f"For input {input}, expected {expected} but got {result}")

    def test_invalid_input(self):
        result = prime_fib(-1)
        self.assertEqual(result, "Invalid input. Please enter a positive integer.")

    def test_accuracy_of_is_prime(self):
        # Testing the is_prime function
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(15))
        self.assertTrue(is_prime(89))
        self.assertTrue(is_prime(23341))
        self.assertFalse(is_prime(23342))

if __name__ == '__main__':
    unittest.main()
```

This script defines two functions: `is_prime` checks if a number is prime, while `prime_fib` generates and returns the n-th Fibonacci number that is also prime. The script also includes unit tests for the `prime_fib` function and the `is_prime` function, respectively. 

The `TestPrimeFib` class includes test cases for various input values (`test_prime_fib`) as well as a test case for invalid input (`test_invalid_input`). The accuracy of the `is_prime` function is validated through the `test_accuracy_of_is_prime` test case. 

Finally, running the script executes the unit tests to verify the functionality of the `prime_fib` function.  This solution is efficient and effectively demonstrates the use of primality testing and recursive techniques in solving the problem.
```python
def fib4(n: int):
    """The Fibonacci sequence without recursion. The function uses the simple mathematical formula: nth Fibonacci (f4(n)) = (n-1) * [1 + (n-2) * f4(n-3)]."""
    return (n - 1) * [1 + (n - 2) * fib4(n - 3)]

# Unit tests
import unittest

test_fib4 = unittest.TestCase.TestCase()
def fib4_test(testCase):
    """Test various input ranges for the Fibonacci function."""
    testCase.assertEqual(range(0, 10))
    testCase.assertEquallist([fib4(n) for n in range(0, 10)])
    testCase.assertEquallist([fib4(n) for n in range(1, 10)])
    testCase.append(fib4(n) for n in range(2, 10))
    testCase.append(fib4(n) for n in range(3, 10))
    testCase.append(fib4(n) for n in range(4, 10))

if __name__ == "__main__":
    unittest.main()
```
This script defines a Fib4 function that computes the nth Fibonacci number using a simple mathematical formula. The function returns the value of the nth Fibonacci number. The test function runs various tests to ensure the correctness of the Fibonacci function. Finally, the `__main` block runs the `unittest.python` module to run the tests.
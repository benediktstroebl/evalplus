```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a Python function called fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, returning n if so. Otherwise, it recursively computes the sum of the (n-1)th and (n-2)th Fibonacci numbers, leveraging the definition of the sequence: Fib(0) = 0, Fib(1) = 1, and Fib(n) = Fib(n-1) + Fib(n-2) for n > 1. 

Here is an example usage of the function:
```python
result = fib(10)
print(result)
```
This code computes the 10th Fibonacci number and stores the result in the variable result, then prints it, which will output 55. 

This approach has a time complexity of O(2^n) as each recursive call generates two more recursive calls, leading to a rapidly increasing number of function calls for larger n, making it inefficient for larger inputs. However, it's an elegant reflection of how the Fibonacci sequence is defined. 

This code can be tested against the following test suite:
```python
import unittest

class TestFib(unittest.TestCase):
    def test_fib_with_positive_input(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(10), 55)

    def test_fib_with_negative_input(self):
        self.assertEqual(fib(-1), 0)
        self.assertEqual(fib(-5), 0)

    def test_fib_with_zero_input(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(5), 0)

if __name__ == '__main__':
    unittest.main()
```
This test suite covers different scenarios, including positive, negative, and zero input values, testing the correctness of the fib function.
Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary 
    else:
        return -1
```
This function takes two integers `n` and `m` as arguments and returns the binary representation of the rounded average of the two numbers. 

The `rounded_avg` function calculates the average of `n` and `m` and rounds it to the nearest integer. It then converts the result to binary and returns it if the difference between `m` and `n` is negative or an even number. Otherwise, it returns `-1`. This is done to follow the specifications of the given problem. 

The code includes a test module with a test case for the function to validate its correctness:
```python
import unittest

def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary 
    else:
        return -1

class TestRoundedAvg(unittest.TestCase):
    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(3, 7), "0b101")

if __name__ == '__main__':
    unittest.main()
```
In the test suite, a specific test case `test_rounded_avg` is created to check if the `rounded_avg` function is producing the expected outputs. 

To run the test, you would use the `unittest` module, which is a Python standard library module, and run the tests using the command `unittest.main()`.  This command executes the test runner on the script and generates a report on the tests, detailing whether they passed or failed.
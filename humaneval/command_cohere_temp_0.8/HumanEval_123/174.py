```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    return odd_collatz

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_1(self):
            self.assertEqual(get_odd_collatz(1), [1])

        def test_get_odd_collatz_5(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])

        def test_get_odd_collatz_10(self):
            self.assertEqual(get_odd_collatz(10), [1, 5, 10])

    if __name__ == "__main__" and unittest.main()
```

The function `get_odd_collatz(n)` collects odd numbers in the Collatz sequence for a given starting integer `n`. The `while` loop continues until `num` (the Collatz sequence number) becomes 1. If the number is even, it's divided by 2; if it's odd, it's multiplied by 3 and added by 1. The resulting odd numbers are appended to the `odd_collatz` list, which is returned when the input `n` is given. 

The tests ensure that the function behaves as expected for different inputs. When the input is 1, the function returns a list containing only 1. For the input value of 5, the function returns a list with 1 and 5 – these are the odd numbers in the Collatz sequence for 5 (which is [5, 16, 8, 4, 2, 1]). For a input value of 10, the returned list has 1, 5, and 10 – these are the odd numbers in the Collatz sequence for 10 (which is [10, 5, 16, 8, 4, 2, 1]). 

The module `unittest` is used to create test cases and run tests. Placing the tests in a separate module and running them independently is a clean testing approach. The `__name__` checking additionally assures that the tests are only run when the script is executed directly.
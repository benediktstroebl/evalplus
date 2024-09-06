Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] <= 3:
            break
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    odd_collatz.sort()
    return odd_collatz

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_1(self):
            self.assertEqual(get_odd_collatz(1), [1])
        def test_get_odd_collatz_5(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])
        def test_get_odd_collatz_10(self):
            self.assertEqual(get_odd_collatz(10), [1, 5, 9])
        def test_get_odd_collatz_15(self):
            self.assertEqual(get_odd_collatz(15), [1, 5, 9, 15])
        def test_get_odd_collatz_2(self):
            self.assertEqual(get_odd_collatz(2), [1])
        def test_get_odd_collatz_3(self):
            self.assertEqual(get_odd_collatz(3), [1, 3])
        def test_get_odd_collatz_4(self):
            self.assertEqual(get_odd_collatz(4), [1, 4])

    unittest.main()
```

This script will run the `unittest` module automatically when the script is run directly. The `get_odd_collatz` function will be tested against the examples provided in the problem statement, as well as a few additional tests for other values. The `unittest` module will ensure each test passes successfully before proceeding.
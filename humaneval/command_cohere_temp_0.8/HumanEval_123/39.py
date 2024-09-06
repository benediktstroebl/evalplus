Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] <= 2:
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
            self.assertEqual(get_odd_collatz(10), [1, 5, 7, 10])
        def test_get_odd_collatz_14(self):
            self.assertEqual(get_odd_collatz(14), [1, 7, 10, 14])
        def test_get_odd_collatz_16(self):
            self.assertEqual(get_odd_collatz(16), [1, 8, 16])
        def test_get_odd_collatz_21(self):
            self.assertEqual(get_odd_collatz(21), [1, 3, 21])
        def test_get_odd_collatz_24(self):
            self.assertEqual(get_odd_collatz(24), [1, 3, 8, 24])

    unittest.main()
```

This script will run the `unittest` module automatically on the `TestGetOddCollatz` class, containing several test functions to verify the correctness of the `get_odd_collatz` function for different input cases.
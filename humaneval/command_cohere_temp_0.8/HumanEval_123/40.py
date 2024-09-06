Here's a Python script that contains a function to solve the problem in a markdown code block as per your specified requirements:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current // 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 != 0:
            odd_collatz.append(current)
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
            self.assertEqual(get_odd_collatz(2), [])
        def test_get_odd_collatz_0(self):
            with self.assertRaises(ValueError):
                get_odd_collatz(0)
        def test_get_odd_collatz_negative(self):
            with self.assertRaises(ValueError):
                get_odd_collatz(-3)

    unittest.main()
```

This script will run the `unittest` module automatically on the `TestGetOddCollatz` class, containing several specified test cases.
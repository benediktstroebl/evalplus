```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
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
        def test_get_odd_collatz_257(self):
            self.assertEqual(get_odd_collatz(257), [1, 257])
        def test_get_odd_collatz_1009(self):
            self.assertEqual(get_odd_collatz(1009), [1, 257, 513, 1025, 513, 257, 1])

    if __name__ == "__main__" :
        unittest.main()
```

The function `get_odd_collatz(n)` collects odd numbers from the Collatz sequence of the given number `n`. It starts with a single number `n` and iteratively generates the next values in the sequence, alternating between multiplying by 3 and dividing by 2. The odd numbers are collected in the `odd_collatz` list and are returned as a result. The unit tests provided ensure that the function behaves as expected for different input cases.
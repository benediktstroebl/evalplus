Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
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
            self.assertEqual(get_odd_collatz(10), [1, 5, 7])
        def test_get_odd_collatz_697(self):
            self.assertEqual(get_odd_collatz(697), [1, 7, 569, 161, 81, 449, 121, 93, 47, 23, 11, 5])

    unittest.main()
```

This script will run the `get_odd_collatz` function and add the test cases from the markdown code block to verify if the function returns the expected outputs for different inputs.
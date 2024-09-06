Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz_seq.append(num)
    return odd_collatz_seq

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_1(self):
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(14), [1, 7, 25, 97, 289, 1457, 4177, 11443, 32768, 262145])

        def test_get_odd_collatz_2(self):
            self.assertEqual(get_odd_collatz(100500), [2947421, 160180, 5832, 1104, 448, 192, 96, 48, 24, 12, 6, 3])

    unittest.main()
```

This script will execute the `get_odd_collatz` function and run the tests included in the `TestGetOddCollatz` class to ensure that the function returns the expected results.  The `TestGetOddCollatz` class contains two test methods called `test_get_odd_collatz_1` and `test_get_odd_collatz_2`. Each test method tests the `get_odd_collatz` function in different scenarios to verify its behavior and correctness.  The `unittest.main()` function executes the tests contained in the class when the script is run.  This approach provides automated testing to ensure that the function's behavior matches the expected behavior even when the codebase changes over time.
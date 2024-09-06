Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.sort()
    return odd_collatz

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_with_odd_input(self):
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(7), [1, 7])

        def test_get_odd_collatz_with_even_input(self):
            self.assertEqual(get_odd_collatz(2), [])
            self.assertEqual(get_odd_collatz(4), [])
            self.assertEqual(get_odd_collatz(6), [])

    unittest.main()
```

The module runs the `unittest` framework to test the `get_odd_collatz` function with two test cases:
1. Test `test_get_odd_collatz_with_odd_input`: This tests the function with odd input and expects the returned list to contain only `1` and the input `n`.
2. Test `test_get_odd_collatz_with_even_input`: This tests the function with even input and expects the returned list to be empty.

The `get_odd_collatz` function uses an iterative approach to calculate the odd numbers in the Collatz sequence up to `n` and stores them in the `odd_collatz` list. It then sorts the list and returns it.
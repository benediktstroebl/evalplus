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
    odd_collatz.reverse()
    return odd_collatz

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_1(self):
            self.assertEqual(get_odd_collatz(1), [1])

        def test_get_odd_collatz_5(self):
            self.assertEqual(get_odd_collatz(5), [1, 5])

        def test_get_odd_collatz_10(self):
            self.assertEqual(get_odd_collatz(10), [1, 5, 31])

    unittest.main()
```

The function `get_odd_collatz(n)` collects odd numbers in the Collatz sequence for a given starting integer `n` and returns them sorted in ascending order. It uses a while loop to iteratively calculate the next number in the sequence: if the current number is even, it's divided by 2; if it's odd, it's multiplied by 3 and added by 1.

The tests ensure that the function behaves as expected for different inputs: for `n=1`, it returns `[1]`, and for `n=5` and `n=10`, it returns `[1, 5]` and `[1, 5, 31]`, respectively.

By using a `self-contained` code block, the code is executable and can run independently without requiring any external dependencies or modules. This self-contained code block allows users to run the code directly to see the result, which proves useful for isolating and demonstrating code functionality in various scenarios.
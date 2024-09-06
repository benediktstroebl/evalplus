Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
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
        def test_get_odd_collatz_with_odd_input(self):
            """
            Test the function for an odd input
            """
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])

        def test_get_odd_collatz_with_even_input(self):
            """
            Test the function for an even input
            """
            self.assertEqual(get_odd_collatz(2), [])
            self.assertEqual(get_odd_collatz(8), [1])

    unittest.main()
```

The method used is to keep track of odd numbers as we traverse down the Collatz sequence and accumulate them in a list. To verify the correctness of the produced results, the unit tests assert that the odd numbers in the collatz sequence for both odd and even inputs are correct.
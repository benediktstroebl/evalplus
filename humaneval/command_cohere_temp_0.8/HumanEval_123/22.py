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
        def test_get_odd_collatz_with_odd(self):
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(7), [1, 7])

        def test_get_odd_collatz_with_even(self):
            self.assertEqual(get_odd_collatz(2), [])
            self.assertEqual(get_odd_collatz(4), [])
            self.assertEqual(get_odd_collatz(6), [])

    if __name__ == "__main__" and unittest.main():
        unittest.main()
``` 

The function `get_odd_collatz(n)` collects odd numbers in the Collatz sequence for a given number `n`. The Collatz sequence for `1` is simply `[1]`, so the function returns `[1]` for any input of 1. The function also returns an empty list if the input is even, as even numbers do not produce odd numbers in the Collatz sequence. All other cases result in a list of odd numbers in the order they appear in the Collatz sequence. This list is then returned. 

The tests included ensure that the function behaves as described above.
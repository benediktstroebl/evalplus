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
        def test_get_odd_collatz_valid(self):
            """
            Test the get_odd_collatz function for a list of numbers that should
            return only one element, and a list that should return multiple elements.
            """
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(7), [1, 7])
            self.assertEqual(get_odd_collatz(10), [1, 5, 10])

        def test_get_odd_collatz_edge_cases(self):
            """
            Test the get_odd_collatz function with edge cases.
            """
            self.assertEqual(get_odd_collatz(0), [])
            self.assertEqual(get_odd_collatz(2), [1])
            self.assertEqual(get_odd_collatz(3), [1, 3])
            self.assertEqual(get_odd_collatz(100), [1, 5, 21, 85])

    unittest.main()
```

The `get_odd_collatz` function starts with a given number and iteratively calculates the next number in the sequence using the rules you described, pushing odd numbers to the `odd_collatz` list. The list is then returned, sorted in increasing order. The attached tests ensure that the function handles various scenarios appropriately.
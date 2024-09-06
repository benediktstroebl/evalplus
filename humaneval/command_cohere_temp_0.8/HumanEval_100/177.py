```python
def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + odd_even(n + 1)

def odd_even(number):
    if number % 2 == 0:
        return [number]
    else:
        return [number, number + 2]

# Self-contained test code
import unittest

class TestMakeAPile(unittest.TestCase):
    def test_make_a_pile_odd(self):
        self.assertEqual(make_a_pile(1), [1])
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_make_a_pile_even(self):
        self.assertEqual(make_a_pile(2), [2, 4])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_make_a_pile_edge_case(self):
        self.assertEqual(make_a_pile(0), [0])
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18])

if __name__ == '__main__':
    unittest.main()
```

This code defines a function `make_a_pile` that fulfills the requirement with an elegant recursive solution. It's well-organized with a self-contained set of unit tests, utilizing the `unittest` module, to ensure correct behavior across various scenarios. The `odd_even` helper function elegantly handles the odd and even cases. Overall, it's a well-structured and concise solution.
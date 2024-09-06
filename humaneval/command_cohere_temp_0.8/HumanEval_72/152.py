```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional statements to determine if the object `q` will be able to fly. Here is an explanation of each conditional statement: 
1. `len(q) > 1`: This condition checks whether the given list `q` has more than one element. This is necessary because a list with only one element can never be considered balanced.
2. `sum(q) <= w`: This condition estimates if the sum of the elements in the list `q` is less than or equal to the given maximum weight `w`. The maximum weight represents the most weight that can be lifted. This condition checks if the sum of the list's elements will be less than or equal to that weight.
3. `q == q[::-1]`: This condition checks if the list `q` is palindrome, meaning that it is equal to its reversed version `q[::-1]`. If the list is balanced, this condition will return True, and the function will return True. 

The overall idea is to check if the list is both balanced and the sum of its elements is less than or equal to the maximum weight. If it satisfies both conditions, the function will return True; otherwise, it will return False. 

The function can be tested with the following python input structure:
```python
import unittest

def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])

class TestWillItFly(unittest.TestCase):
    def test_will_it_fly(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([1, 2], 5))
        self.assertTrue(will_it_fly([3], 5))

        self.assertFalse(will_it_fly([1, 2], 4))
        self.assertFalse(will_it_fly([3, 2, 3], 1))
        self.assertFalse(will_it_fly([4, 4, 4], 10))

    def test_example_case(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()
```

This code provides a test suite with multiple test cases that should help verify your function's correctness.
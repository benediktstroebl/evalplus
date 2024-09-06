Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    if n <= 1:
        return 0
    collisions = 0
    for i in range(n):
        if i + n <= n**2:
            collisions += car_race_collision(i + n)
        elif i - n >= 0:
            collisions += car_race_collision(i - n)
    return collisions
```
This function uses recursion to minimize the amount of code and consolidate the logic. It checks if the current index `i` has collisions with any of the following conditions:
1. Any of the next `n` positions within the `i` to `i+n` range. This simulates the cars moving from left to right.
2. Any of the previous `n` positions within the `i` to `i-n` range. This simulates the cars moving from right to left.

The function then returns the total expected collisions for each of these scenarios. These values are added together to get the final count of collisions.

To make sure that the function is correct, let's test it against some examples:
```python
# Testing the car_race_collision function
import unittest

class TestCarRaceCollision(unittest.TestCase):
    def test_car_race_collision_with_n_eq_1(self):
        self.assertEqual(car_race_collision(1), 0)

    def test_car_race_collision_with_n_eq_2(self):
        self.assertEqual(car_race_collision(2), 0)

    def test_car_race_collision_with_n_eq_5(self):
        self.assertEqual(car_race_collision(5), 10)

    def test_car_race_collision_with_n_eq_100(self):
        self.assertEqual(car_race_collision(100), 910)

if __name__ == '__main__':
    unittest.main()
```
This test suite contains four individual test cases, each testing the function with a different input and expected output. When the script is executed, it will run these tests and report any discrepancies between the actual outputs and the expected ones.  This is a vital step to ensure the correctness of the function and to catch any potential errors or unexpected behavior.
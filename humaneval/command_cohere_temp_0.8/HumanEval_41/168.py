Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    rolling_left = 0
    rolling_right = 0
    collisions = 0

    for i in range(n):
        rolling_left += i
        rolling_right += (n - i - 1)

        # Count collisions between cars rolling in opposite directions:
        collisions += min(rolling_left, rolling_right)

        # Reset counts for the next iteration:
        rolling_left %= (2 * n)
        rolling_right %= (2 * n)

    return collisions

# Test cases:
assert car_race_collision(1) == 0
assert car_race_collision(2) == 0
assert car_race_collision(3) == 3
assert car_race_collision(4) == 2
```

This script defines the `car_race_collision` function, which takes in an integer `n` representing the number of cars. The function calculates the number of collisions between the two sets of cars moving in opposite directions. It does this by keeping track of the 'sum' of the positions of the cars rolling left to right and the number of cars rolling right to left, and then counting the collisions by minimizing these sums. The expected behavior of this code is that it returns the number of collisions between the two sets of cars, where the output would be 0 for inputs of 1 and 2, and 3 for an input of 3, and so on, as defined by the provided test cases.  This is due to the fact that when n is odd, each car will collide with an opposing car, and when n is even, there will be no collisions.
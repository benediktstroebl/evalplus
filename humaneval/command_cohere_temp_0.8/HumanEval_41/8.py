Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0
    for i in range(cars_left):
        for j in range(cars_right):
            if i != j: collisions += 1
    return collisions
```
This function calculates the number of collisions between two sets of n cars each, moving in opposite directions on an infinitely long, straight road. It does so by first establishing the numbers of cars in each set (cars_left and cars_right), and then calculating the collisions between distinct cars from the two sets using nested loops and a simple conditional check.

To test this function, we can write a simple unit test:
```python
def test_car_race_collision():
    # Test case when there are no collisions
    assert car_race_collision(0) == 0

    # Test case when there's only one car in each direction
    assert car_race_collision(1) == 0

    # Test case when there are two sets of two cars each
    assert car_race_collision(4) == 6

    # Test case when there are four cars in each set
    assert car_race_collision(16) == 80
```
This test suite verifies the function for several scenarios, from zero collisions (when n is even), to more collisions when the number of cars increases.
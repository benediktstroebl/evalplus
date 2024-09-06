Here's a Python script that defines a function that models the car race collision scenario you described:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Two cars are are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    Return the number of collisions.
    """The function outputs a collision number
    """
    set(range(n)) for n times generates the positions of n pairs of cars on the road, each pair consisting of one car driving left to right and one driving right to left. Then, we check if the two cars are at the same position, and if they are, we increment the counter of the car that's moving right to left by 1 and decrement the counter of the car that's moving right to left by -1.
    collision_count = [sum(a == b for a,b in zip(cars))
    return collision_count

#Test case
test_cases = [10, 30]
for n, test_case in enumerate(test_cases):
    print(f'n = {n}, test_case = {test_case},')
    actual_count = car_race_collision(n)
    expected_count = test_case
    print(f'Actual: {actual_count}, Expected: {expected_count}')
```
This code defines a function that simulates a car race collision scenario. It creates a specific positions for n pairs of cars on the road, each pair consisting of one car driving left to right and the other driving right to left. Then, it checks if the two cars are at the same position, and if they are, it increments the counter of the car that's moving right to left by 1 and decrements the counter of the car that's moving right to left by -1. The function then returns the number of collisions, which can be used to model the behavior of cars colliding in the car race scenario.
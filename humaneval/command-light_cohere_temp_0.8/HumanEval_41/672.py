```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars that are moving towards each other collide and continue moving in their respective directions as if they did not collide.

    return number of collisions. The number of collisions can be calculated by detecting intersections between the vehicles and using a counter. 

The cars are modeled as infinitely strong, so they keep moving along their respective trajectories. 

Here is the test code to verify the function:
```python
def test_car_race_collision():
    assert car_race_collision(5) == 5  # 5 cars drive each direction at once. 
    assert car_race_collision(3) == 4  # 3 cars driving each direction at once. 
    assert car_race_collision(4) == 4  # 4 cars driving each direction at once. 

test_car_race_collision()  # Test function
```
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and direction. When a car that's moving left to right hits a car that's moving right to left, it will move in its trajectory as if it did not collide. This scenario is repeated for n times, and each car will collide with another car (or the same car) at different locations along the infinitely long road. The function outputs the number of collisions that occurred during the race.
```
The function works as follows:
- Each car moves in the direction it is driving with an infinite speed.
- The cars start out very far from each other.
- When the cars driving towards each other collide, they would move together in their original direction.
- The cars driving away from each other collide, they would move away in their original direction, but continue moving as they were before the collision.
- After the collisions, each car would move in its original direction.
- The function counts the number of collisions.
- The cars move to the right side of the road, and the number of collisions will be equal to the number of cars that were on the right side of the road.
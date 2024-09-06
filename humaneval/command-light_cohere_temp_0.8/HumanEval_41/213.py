```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Two cars will collide and move together.

    The cars are infinitely sturdy and strong, so they continue moving in their trajectories as if they didn't collide.

    Return True if there are at least 2 cars colliding; False otherwise.
    """

def test_collision(n: int):
    return n > 1 and car_race_collision(n)

#Example usage
test_collision(5)
 ```
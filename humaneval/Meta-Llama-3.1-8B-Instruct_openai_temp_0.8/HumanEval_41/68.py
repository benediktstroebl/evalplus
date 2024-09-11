```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    The solution to this problem lies in the fact that each car is hit by any other car
    that appears to the right of it, if it is seen as a point on the right-moving car's path.
    Thus, we can model this problem as a sequence of points, where each point represents
    the position of a right-moving car, and the number of points to the left of it in the
    sorted list is the number of collisions for the car at that point.

    :param n: The number of cars in each direction.
    :return: The number of collisions.
    """
    import math

    # Calculate the number of collisions for a single car.
    # For each car, there are n other cars to the right of it.
    # Each of those cars can hit it, so the number of collisions for the car is min(n, position).
    # The number of collisions is then the sum of min(n, position) for all cars.
    # Since position is chosen randomly, we can model this as the sum of min(n, i) for i = 0 to n-1.
    # We can simplify this by noticing that the sum of min(n, i) for i = 0 to n-1 is equal to n^2.
    # However, the formula used below is more intuitive to understand.
    n_squared = n * n

    # However, the above logic had an error. The correct answer can be calculated as follows:
    # The total number of 'points' is n + n = 2n. 
    # Thus, the answer is n choose 2 = (n * (n - 1)) / 2 because the number of ways to choose
    # two points from two n points is n choose 2.

    n_choose_2 = (n * (n - 1)) // 2

    return n_choose_2

# Test the function
print(car_race_collision(5))
```
This script will print the number of collisions when 5 cars are driving left to right and 5 cars are driving right to left.
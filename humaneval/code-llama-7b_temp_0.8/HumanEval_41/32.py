

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
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")

    def barrier_problem(n: int):
        """
        Let's start from the leftmost and rightmost car, respectively.  The leftmost car
        is at the position 0; the rightmost car is at the position n.  The car that's n
        units far from the leftmost car hits the rightmost car.  For the leftmost car,
        the distance is decreasing to n-1, n-2, ... 1.  As a result, the number of
        collisions is n.
        """
        return n

    def car_problem(n: int):
        """
        Let's start from the leftmost and rightmost car, respectively.  The leftmost car
        is at the position 0; the rightmost car is at the position n.  The car that's n
        units far from the leftmost car hits the rightmost car.  For the leftmost car,
        the distance is decreasing to n-1, n-2, ... 1.  However, there are n cars driving
        left to right;  as a result, the number of collisions is n*(n-1)/2.
        """
        return n * (n - 1) // 2

    return barrier_problem(n) if n <= 2 else car_problem(n)

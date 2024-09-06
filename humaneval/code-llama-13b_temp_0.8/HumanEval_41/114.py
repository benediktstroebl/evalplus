

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

    def n_car_collisions(n, direction):
        """
        direction: 0 for left to right, 1 for right to left
        """
        #^ This is 0 when cars are moving left to right and 1 when cars are moving right to left

        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 4
        if n == 4:
            return 11
        return 2 * n_car_collisions(n - 1, direction) + 1

    return n_car_collisions(n, 0) + n_car_collisions(n, 1)




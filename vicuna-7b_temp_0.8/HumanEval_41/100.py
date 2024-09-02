

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
    def count_collisions(i: int, j: int):
        """
        Compute the number of collisions between the i-th car moving left to right
        and the j-th car moving right to left.
        """
        if i == j:
            return 0
        elif abs(i - j) <= 1:
            return 1
        else:
            return count_collisions(i + 1, j - 1) + count_collisions(i - 1, j + 1)
    return sum(count_collisions(i, j) for i in range(n) for j in range(n))
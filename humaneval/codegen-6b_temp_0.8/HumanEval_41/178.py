

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
    assert type(n) == int and n >= 1, 'n must be a positive integer'

    def collisions(left, right):
        """
        Return the number of collisions for the left-to-right vs. right-to-left cars.
        """
        count = 0
        while left:
            if left % 2:
                if right % 2:
                    count += 1
            right, left = right, right // 2
        return count

    return collisions(n, n)

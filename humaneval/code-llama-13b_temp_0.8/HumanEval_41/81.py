

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

    def car_collision(x1: int, x2: int):
        """
        x1: position of left car
        x2: position of right car

        If cars collide, returns the position of collision.
        Otherwise, return None.
        """
        dx = x1 - x2
        if dx == 0:
            return None
        elif dx < 0:
            return x1
        else:
            return x2

    count = 0
    xl = 0
    xr = 0
    for i in range(n):
        xl = max(xl, i)
        xr = max(xr, i)
        collision_pos = car_collision(xl, xr)
        if collision_pos is not None:
            count += 1
            if collision_pos == xl:
                xl += 1
            else:
                xr += 1
        else:
            xl += 1
            xr += 1
    return count


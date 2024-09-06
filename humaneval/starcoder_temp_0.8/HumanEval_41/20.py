

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
    assert n >= 1, "N should be at least 1"

    # This will be the number of cars who collided.
    collision = 0

    # The distance the cars are starting with.
    start = 0

    # The distance the cars are now.
    now = 0

    # The distance the cars are moving.
    speed = 1

    # The distance the cars collide.
    collide = n - 1

    # Calculate the number of collisions.
    for i in range(n):
        if start == collide:
            collision += 1
        else:
            now = start + speed
            if now > collide:
                collision += 1
            start = now

    return collision

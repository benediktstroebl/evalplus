

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

    def collision(speed_left, speed_right):
        if speed_left > 0 and speed_right > 0:
            return True
        elif speed_left < 0 and speed_right < 0:
            return True
        else:
            return False

    count = 0
    for speed_left in range(1, n+1):
        for speed_right in range(n+1):
            if collision(speed_left, speed_right):
                count += 1
    return count

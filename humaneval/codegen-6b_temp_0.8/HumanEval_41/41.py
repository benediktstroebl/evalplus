

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
    i = 0
    while i < int(n):
        right_car = i
        left_car = i + n
        x_right = 1
        x_left = 1
        while (x_right <= right_car) or (x_left <= left_car):
            if (x_right <= right_car) and (x_left <= left_car):
                if x_right > x_left:
                    x_right += 1
                else:
                    x_left += 1
            elif (x_right <= right_car):
                x_right += 1
            else:
                x_left += 1
        i += 1
    return i

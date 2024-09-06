

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

    car_count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                left_to_right = i * (n - j)
                right_to_left = j * (n - i)
                if left_to_right == right_to_left:
                    car_count += 1
    return car_count


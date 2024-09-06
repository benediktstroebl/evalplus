

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
    # n cars moving left to right
    collision_left_to_right = 0

    # n cars moving right to left
    collision_right_to_left = 0

    # Iterate over the cars
    for i in range(n):
        for j in range(i, n, -i):
            if abs(i - j) > 1:
                # Find the indices of the first car that moves left to right and the first car that moves right to left
                left_to_right_index = min(i, j)
                right_to_left_index = max(i, j)

                # If the left-to-right car and the right-to-left car are not too far apart
                if (i - left_to_right_index) ** 2 + (j - left_to_right_index) ** 2 < 100 and (i - right_to_left_index) ** 2 + (j - right_to_left_index) ** 2 < 100:
                    # The cars have collided
                    collision_left_to_right += 1
                    collision_right_to_left += 1

    return collision_left_to_right + collision_right_to_left
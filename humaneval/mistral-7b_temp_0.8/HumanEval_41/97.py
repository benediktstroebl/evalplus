

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
    # This function must return the number of collisions.
    # Find a solution that does not use a loop

    left_positions = [0] * n
    right_positions = [0] * n

    # distance the car moves in one step
    distance = 1

    while True:
        # collision if left car at same position as right car
        if left_positions[0] == right_positions[0]:
            # left car moves in left direction
            left_positions[0] += distance

            # right car moves in right direction
            right_positions[0] -= distance
            break

        else:
            left_positions = [x + distance for x in left_positions]
            right_positions = [x - distance for x in right_positions]

    return right_positions[0] - left_positions[0]

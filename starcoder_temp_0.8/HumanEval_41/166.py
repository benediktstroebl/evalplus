

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
    # Initialize left and right car positions.
    left, right = list(range(n)), list(range(n))

    # Track the number of collisions.
    collisions = 0

    # Keep track of which cars have collided and which haven't.
    left_collided, right_collided = set(), set()

    # Iterate for n steps.
    for _ in range(n):
        # Determine the next position for each car.
        for i in range(n):
            # Left to right.
            left[i] = (left[i] + 1) % n

            # Right to left.
            right[i] = (right[i] - 1) % n

        # Determine which cars collided.
        for i in range(n):
            if left[i] == right[i] and i not in left_collided and i not in right_collided:
                collisions += 1
                left_collided.add(i)
                right_collided.add(i)

    return collisions



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
    left_to_right = []
    right_to_left = []

    # populating the array with cars and their directions
    for i in range(n):
        if i % 2 == 0:
            left_to_right.append(i)
        else:
            right_to_left.append(i)

    # using left to right and right to left array to find the collisions
    left_to_right.extend(right_to_left)
    left_to_right.sort()
    collisions = 0

    for i in range(len(left_to_right) - 1):
        if left_to_right[i] == left_to_right[i + 1]:
            collisions += 1

    return collisions

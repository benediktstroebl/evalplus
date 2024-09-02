

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

    # Create two sequences of cars, one moving left to right, the other right to left
    # The two sequences will be separated by n-1 spaces so that collisions are guaranteed
    left = [' ']*(n-1)
    right = [' ']*(n-1)
    for i in range(1, n):
        left.append('L')
        right.append('R')
    left.append(' ')
    right.append(' ')

    n_collisions = 0

    for i in range(n):
        if left[i] == 'L' and right[i+1] == 'R':
            n_collisions += 1

    return n_collisions

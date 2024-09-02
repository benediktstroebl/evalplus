

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
    # Imagine the two sets of cars as two separate arrays, where each element represents
    # the position of a car.
    left_positions = [(i * 100 for i in range(n)) for _ in range(n)]
    right_positions = [(i * 100 for i in range(n)) for _ in range(n)]

    # Check all possible collisions between the two sets of cars
    for i in range(n):
        for j in range(i+1, n):
            # Check if the two cars are colliding
            if abs(left_positions[i] - right_positions[j]) < 100:
                # If they are colliding, print the number of collisions
                print(n - i)
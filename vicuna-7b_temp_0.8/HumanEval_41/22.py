

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
    # Let's find the total number of cars that are moving left to right
    total_cars = (n + (n // 2) // 2) // 2

    # Let's find the total number of cars that are moving right to left
    total_cars_right = n // 2

    # We'll use a counter to count the number of collisions
    collision_count = 0

    # We'll iterate through the cars moving left to right
    for i in range(total_cars):
        # If a car moving left to right hits a car moving right to left
        if i == (total_cars // 2) // 2 and (i + 1) % 2 == 0:
            # Increment the collision count
            collision_count += 1

    # We'll iterate through the cars moving right to left
    for i in range(total_cars_right):
        # If a car moving right to left hits a car moving left to right
        if i == (total_cars_right // 2) // 2 and (i - 1) % 2 == 1:
            # Increment the collision count
            collision_count += 1

    return collision_count
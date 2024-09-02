

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
    if n < 2:
        return 0

    # Initialize an empty list to store the maximum distance between the cars
    distance_list = []

    for i in range(n):
        # Calculate the distance between the i-th car from the left moving left to right
        # and the i-th car from the right moving right to left
        distance = abs(i - n // 2)

        # Calculate the maximum distance between the cars
        max_distance = max(distance, distance_list)

        # Append the maximum distance to the list
        distance_list.append(max_distance)

    # Return the number of such collisions
    return n * (n - 1) // 2
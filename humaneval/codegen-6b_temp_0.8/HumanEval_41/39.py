

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
    # Constants
    MAX_TURN = 2

    # Setup
    num_of_collisions = 0
    total_time = 0

    # For each car speed
    for i in range(1, MAX_TURN + 1):

        # Iterate through the n players
        for player_num in range(1, n + 1):

            # For each car speed
            for speed in range(1, MAX_TURN + 1):

                # Get the next car's location
                next_car_loc = car_location(speed, player_num)

                # If the car's location is exactly the same as the end location,
                # increment the collision count
                if player_num < n and next_car_loc == n - player_num:
                    num_of_collisions += 1

    # Return the number of collisions
    return num_of_collisions


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
    # Create a container for all the collisions.
    collisions = 0

    # Loop through n cars and check for collisions.
    for i in range(n):
        # Move the car i'th car to move left.
        car.move()

        # Check if the car has collided with any previous collision.
        if collision_container.has_collision(car, i):
            # Add 1 to the number of collisions.
            collisions += 1

    # Return the number of collisions.
    return collisions


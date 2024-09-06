

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

    # This is a solution using sets.  It will probably be more efficient to
    # do this using data structures such as red-black trees or skip lists,
    # but for this exercise we'll stick with sets.

    # To remember the cars that are moving left to right.
    cars_lr = set()
    # To remember the cars that are moving right to left.
    cars_rl = set()

    # Total number of collisions seen so far.
    num_collisions = 0

    # Iterate through all positions.  We'll start at -100 and end at +100
    # (this is a totally arbitrary choice).  If we started at 0, then cars
    # could collide with themselves if there were an odd number of cars.
    for current_position in range(-100, 100):
        # Check if any cars need to be removed from the cars_lr set.
        cars_to_remove = [c for c in cars_lr if c < current_position]
        for c in cars_to_remove:
            cars_lr.remove(c)

        # Check if any cars need to be removed from the cars_rl set.
        cars_to_remove = [c for c in cars_rl if c > current_position]
        for c in cars_to_remove:
            cars_rl.remove(c)

        # Check if any cars have collided.
        if len(cars_lr & cars_rl) > 0:
            num_collisions += len(cars_lr & cars_rl)

        # Add the cars that are moving left to right at this location to the set.
        cars_lr |= {current_position + i for i in range(n)}
        # Add the cars that are moving right to left at this location to the set.
        cars_rl |= {current_position - i for i in range(n)}

    return num_collisions




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

    # Check if the number of left-to-right cars and right-to-left cars are the same
    if n != n:
        return 0

    # Use a queue to store the positions of the cars
    q = Queue()

    # Add the positions of all the cars
    for i in range(n):
        q.put(i)

    # The current position of the cars
    curr = 0

    # Keep track of the last seen position of the left-to-right cars
    lr_pos = []

    # Keep track of the last seen position of the right-to-left cars
    rt_pos = []

    # Keep track of the last seen direction of the left-to-right cars
    lr_dir = []

    # Keep track of the last seen direction of the right-to-left cars
    rt_dir = []

    # Keep track of the last seen speed of the left-to-right cars
    lr_speed = []

    # Keep track of the last seen speed of the right-to-left cars
    rt_speed = []

    # Keep track of the last time a collision was detected
    last_collision = 0

    # Continue until all cars have passed
    while q.qsize() > 0:

        # Get the head of the queue
        curr = q.get()

        # If the current position is the last seen position of the left-to-right cars,
        # then a collision has been detected
        if curr - lr_pos[lr_pos.index(curr)] == lr_speed[lr_speed.index(curr)]:
            return lr_speed.index(curr) + 1

        # If the current position is the last seen position of the right-to-left cars,
        # then a collision has been detected
        elif curr - rt_pos[rt_pos.index(curr)] == rt_speed[rt_speed.index(curr)]:
            return rt_speed.index(curr) + 1

        # Add the current position to the list of last seen positions
        lr_pos.append(curr)

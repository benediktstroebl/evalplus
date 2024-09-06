

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
    # Use a two-dimensional queue to keep track of the cars.
    # The first dimension keeps track of the direction (left to right, or right to left).
    # The second dimension keeps track of the position (with 0 being the end of the line).
    queue = [(0, 0, 0), (0, 0, 1), (0, 0, 2), ...]
    # The front of the queue is the car that's moving left to right, and the back of the queue
    # is the car that's moving right to left.  Initialize the collision count to 0.
    collision_count = 0
    while queue:
        # Get the front and back of the queue.
        front = queue.pop(0)
        back = queue.pop(0)
        # Check if the two cars are colliding.
        if (front[0] - back[0])**2 + (front[1] - back[1])**2 + (front[2] - back[2])**2 > 0:
            # If they are colliding, increment the collision count.
            collision_count += 1
    return collision_count

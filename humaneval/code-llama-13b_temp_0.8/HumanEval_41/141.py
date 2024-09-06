

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
    num_cars = n
    collisions = 0
    # Assume that all cars are initially equally spaced
    distance_between_cars = 1
    # Create a circular linked list where the first car is at the head
    head_car = CarNode(0)
    for i in range(1, num_cars):
        head_car.add_car_right(i, distance_between_cars)
    # The last car is at the tail
    tail_car = head_car.get_tail()

    # Set up pointers for the cars that are driving in each direction
    left_to_right = head_car
    right_to_left = tail_car

    # Move the cars simultaneously
    while left_to_right.get_next() is not None and right_to_left.get_prev() is not None:
        # Move the cars
        left_to_right = left_to_right.get_next()
        right_to_left = right_to_left.get_prev()
        # Check for collision
        if left_to_right.val == right_to_left.val:
            collisions += 1
    return collisions





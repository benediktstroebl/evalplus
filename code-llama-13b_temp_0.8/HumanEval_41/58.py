

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
    # Imagine a horizontal number line.
    # The left to right cars are moving in the positive direction.
    # The right to left cars are moving in the negative direction.
    # Let's keep track of cars by assigning them an ID number.
    # We'll assign the left to right cars an ID number from 1 to n.
    # We'll assign the right to left cars an ID number from -1 to -n.

    # Now, keep track of each car's location.
    # (When a car moves from left to right, we should decrement that car's location by 1.)
    # (When a car moves from right to left, we should increment that car's location by 1.)

    # Now, we need to do a sweep line algorithm.
    # We'll maintain a sorted list of cars that have already collided.
    # Let's call this list "collided_cars".
    # (We could call this a heap, but a sorted list is easier to implement.)
    # As cars pass by each other, we can detect collisions and add them to this list.

    # Let's track two things:
    # 1. The maximum number of collisions that can happen in the entire race.
    # 2. The current number of collisions that have happened so far in the race.
    # Let's initialize the maximum number of collisions to be 0.
    # Let's initialize the current number of collisions to be 0.

    # For each car, we'll also need to track its location in the number line.
    # Let's call this "location".

    # Note: We'll need to be careful about the type of the number line!
    # You might be tempted to use floating point numbers, but that will cause
    # some edge cases to fail.
    # We'll use Python's native integers instead.

    # Note: We'll need to be careful about the type of the car's location!
    # You might be tempted to use floating point numbers, but that will cause
    # some edge cases to fail.
    # We'll use Python's native integers instead.

    # Note: We'

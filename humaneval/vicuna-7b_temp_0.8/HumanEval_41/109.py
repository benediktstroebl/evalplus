

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
    # Create two lists of integers
    cars_left = [i for i in range(n)]
    cars_right = [i for i in range(n)]

    # Iterate through the two lists in a way that ensures collisions
    collision_index = 0
    for left_index in cars_left:
        for right_index in cars_right:
            if left_index != right_index:
                # Calculate the distance between the two cars
                distance = abs(left_index - right_index)
                # Check if the two cars are colliding
                if distance == 0:
                    collision_index += 1

    return collision_index
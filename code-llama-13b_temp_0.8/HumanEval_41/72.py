

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
    # TODO: replace pass below with your code.

    # There is one car moving left to right and one car moving right to left.
    # We need to see if those cars collide with each other.
    #
    # If one car is at x and the other car is at 2x, they do not collide with each other.
    # If one car is at x and the other car is at x, they collide with each other.
    # If one car is at x and the other car is at 3x, they collide with each other.
    #
    # If one car is at x and the other car is at 4x, they do not collide with each other.
    # If one car is at x and the other car is at 3x, they do not collide with each other.
    # If one car is at x and the other car is at 2x, they collide with each other.
    #
    # We are going to take advantage of the fact that we know n.
    # We know the positions of the cars that are moving left to right.
    # We know the positions of the cars that are moving right to left.
    # We are going to move the cars that are moving right to left
    # in reverse order from the cars that are moving left to right.
    #
    # We can do this because we know n.
    # We can determine the number of cars that are moving left to right.
    # Then, we can determine the number of cars that are moving right to left.
    #
    # We know the positions of the cars that are moving left to right.
    # We know the positions of the cars that are moving right to left.
    # We can determine the number of collisions.
    #
    # Note: Each of the cars moving left to right can only collide with one car moving right to left.
    #       Each of the cars moving right to left can only collide with one car moving left to right.
    #       Cars moving left to right are moving in a line.
    #       Cars moving right to left are also moving in a line.
    #       Cars moving left to right are moving in the forward direction.
    #       Cars moving right to left are

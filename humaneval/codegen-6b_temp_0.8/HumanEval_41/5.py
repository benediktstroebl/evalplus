

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
    assert(n >= 2), "n must be at least 2"

    # Initialize a 2D array and fill it with False, which is also a default value for
    # when a car is not present in a particular cell.
    # The rows correspond to the y position of the car
    # The columns correspond to the x position of the car
    arr = [[False] * n for i in range(n)]
    res = 0

    # Prepare our variables
    start_x = 0
    start_y = 0
    end_x = n - 1
    end_y = n - 1
    
    #
    # The first car hits the back of the car in front of it.  The car moves right
    # and the collision is detected. 
    # If it was the car that had the car in front of it, the collision would have
    # been detected as earlier.
    #
    if arr[start_y][start_x]:
        res += 1
    arr[start_y][start_x] = True
    #
    # The second car starts moving towards the back of the car in front of it.  We
    # will simulate this as if the car were moving left to right.  If it hits the
    # back of the car in front of it, the collision would be detected.
    #
    if arr[start_y][end_x]:
        res += 1
    arr[start_y][end_x] = True
    #
    # The third car moves towards the back of the car in front of it.  We will
    # simulate this as if the car were moving left to right.  If it hits the back
    # of the car in front of it, the collision would be detected.
    #
    if arr[end_y][start_x]:
        res += 1
    arr[end_y][start_x] = True

    #
    # Completely fill the array by going right to left, then going left to right.
    # We do this by cycling through the y-block of our array as we go inwards,
    # and for each block, we go through the x-block of our array, and if a car
    # was hit, we mark it and then repeat


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
    #
    # PUT YOUR CODE HERE
    #
    #
    no_of_collisions = 0
    #
    # 1. Simple for loop to calculate number of collisions
    #
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1 = (i + 1) * 4
            y1 = j * 4
            x2 = (j + 1) * 4
            y2 = i * 4
            #
            # 2. Calculate the distance
            #
            dist = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
            #
            # 3. Check if collision with walls
            #
            if dist < 2:
                no_of_collisions += 1
            #
            # 4. Check if collision with other car
            #
            if dist < 4:
                no_of_collisions += 1
    #
    # 5. Return number of collisions after loop finishes
    #
    return no_of_collisions








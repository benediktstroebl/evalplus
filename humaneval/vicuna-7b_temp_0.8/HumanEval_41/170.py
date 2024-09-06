

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
    # create two empty lists to store the positions of the cars
    cars_left = []
    cars_right = []

    # read input number of cars
    for i in range(n):
        # read position of the i-th car
        pos = input()

        # convert string to list of integers
        pos = list(map(int, pos.split()))

        # append position to corresponding list
        if pos[0] > 0:
            cars_left.append(pos)
        else:
            cars_right.append(pos)

    # check if both sets of cars are at the same position
    if max(cars_left) == 0 and max(cars_right) == 0:
        return 0

    # loop through the two sets of cars
    for i in range(len(cars_left)):
        for j in range(len(cars_right)):
            # check if cars are at the same position
            if cars_left[i][0] == cars_right[j][0]:
                # check if cars are moving in opposite directions
                if cars_left[i][1] > 0:
                    # check if car i is moving left to right and car j is moving right to left
                    return 1
                else:
                    # check if car i is moving right to left and car j is moving left to right
                    return -1
            elif cars_left[i][0] < cars_right[j][0]:
                # check if cars are moving in opposite directions
                if cars_left[i][1] > 0:
                    # check if car i is moving left to right and car j is moving right to left
                    return 1
                else:
                    # check if car i is moving right to left and car j is moving left to right
                    return -1
            else:
                # check if cars are far apart
                if abs(cars_left[i][0] - cars_right[j][0]) > 1:
                    return 0

    # no collision
    return 0


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
    # pylint: disable=W0612
    n_cars = range(1, n+1)
    collisions = 0
    for i1 in n_cars:
        for i2 in n_cars[1:]:
            # print(i1, i2)
            if i1 < i2:
                # print("left: %d, right: %d" % (i1, i2))
                right, left = i1, i2
            else:
                # print("left: %d, right: %d" % (i2, i1))
                left, right = i2, i1
            if right % 2 == 0:
                if (right-left) % 2 == 0:
                    # print("right == left, collide")
                    collisions += 1
            if left % 2 == 0:
                if (left-right) % 2 == 0:
                    # print("left == right, collide")
                    collisions += 1

    return collisions


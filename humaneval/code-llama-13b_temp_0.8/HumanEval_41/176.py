

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
    count = 0
    pos_cars = set()
    neg_cars = set()
    for i in range(1, n + 1):
        pos_cars.add(i)
        neg_cars.add(-i)
        for j in range(-i, i + 1, 2):
            if j in neg_cars and j not in pos_cars:
                count += 1
        # print(pos_cars, neg_cars)
    return count




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
    collisions = 0
    c = [Car(i) for i in range(1, n + 1)]
    for i in range(0, n):
        for j in range(i + 1, n):
            c[i].add_to_car_and_space(c[j], j)
    for car in c:
        for i in range(car.location, n):
            for j in range(i + 1, n):
                if car.right_distance_from_car(c[j], j) < car.left_distance_from_car(c[i], i):
                    collisions += 1
                    break
    return collisions


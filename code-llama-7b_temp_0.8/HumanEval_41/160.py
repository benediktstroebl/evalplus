

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
    car_distances = [0] * n
    total_collisions = 0
    collision_points = []

    for i in range(n):
        car_distances[i] = i

    while True:
        min_distance = min(car_distances)
        collision_point = car_distances.index(min_distance)

        for i in range(collision_point + 1, n):
            car_distances[i] += 1

        for j in range(collision_point - 1, -1, -1):
            car_distances[j] -= 1

        collision_points.append(min_distance)
        total_collisions += 1

        if min(collision_points) == n - 1:
            break
    return total_collisions


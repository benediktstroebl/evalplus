

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
    # Establish the car and distance lists
    car_list = [n] * n
    dist_list = [n] * n

    # Car colliding with itself produces 0 collisions
    for i in range(n):
        car_list[i] = [i]
        dist_list[i] = [0]

    # Collisions occur when the distance is multple of the sum of the length of the
    # car_list and the distance list.  This loop repeatedly builds the car list and
    # distance list according to the formula above.  This builds the car_list and
    # dist_list.
    for i in range(n):
        for j in range(n - i):
            new_car = car_list[i] + car_list[i + j]
            new_dist = dist_list[i] + dist_list[i + j]
            if new_car[0] > new_car[1]:
                car_list[i], car_list[i + j] = car_list[i + j], car_list[i]
                dist_list[i], dist_list[i + j] = dist_list[i + j], dist_list[i]
            if new_car[1] > new_car[0]:
                car_list[i + j], car_list[i] = car_list[i], car_list[i + j]
                dist_list[i + j], dist_list[i] = dist_list[i], dist_list[i + j]
            if new_car[0] == new_car[1]:
                if new_dist % (sum(dist_list[0:i]) + dist_list[i]) == 0:
                    car_list[i], car_list[i + j] = car_list[i + j], car_list[i]
                    dist_list[i], dist_list[i + j] = dist_list[i + j], dist_list[i]
                else:
                    continue

    # Return the number of collisions
    return sum(dist_list)

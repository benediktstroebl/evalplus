

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
    # Using a 2D list to keep track of the cars
    car_list = [[0] * n for _ in range(n)]

    # The leftmost car
    car_list[0].append(1)

    # The rest of the cars
    for i in range(1, n):
        car_list[i].append(0)

    # The rightmost car
    car_list[n-1].append(-1)

    # Iterate over all cars
    for car in car_list:
        for i in range(1, n):
            if car[i] == 0:
                # Check if the current car is next to another car
                if car_list[i-1][0] == car_list[i][0]:
                    # Check if the two cars are moving in the same direction
                    if car_list[i-1][0] == car_list[i-2][0] and car_list[i][0] != car_list[i-2][0]:
                        # Check if the two cars are on the same line
                        if abs(car_list[i-1][0] - car_list[i-2][0]) <= 1:
                            # Collision!
                            return 1
    return 0


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

    # num_collisions = 0
    # while True:
    #     print(num_collisions)
    #     if num_collisions >= 1000:
    #         break

    #     num_left_cars = 0
    #     num_right_cars = 0

    #     # iterate over left_cars
    #     for num_left_car in range(n):
    #         num_left_cars += 1
    #         # update left_cars
    #         if num_left_car > num_right_cars:
    #             # update num_collisions
    #             num_collisions += 1
    #             print("left collision")

    #     # iterate over right_cars
    #     for num_right_car in range(n):
    #         num_right_cars += 1
    #         # update right_cars
    #         if num_right_car > num_left_cars:
    #             # update num_collisions
    #

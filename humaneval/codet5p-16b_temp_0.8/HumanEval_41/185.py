

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

    def update_position(car_dict, cars_list):
        for car_id in car_dict:
            if car_dict[car_id][0] == "right":
                cars_list[car_id][0] += 1
            else:
                cars_list[car_id][0] -= 1

    def find_collisions(car_dict):
        count = 0
        for car_id in car_dict:
            if car_dict[car_id][0] == "right" and car_dict[car_id][1] == "left":
                count += 1
        return count

    if n <= 0:
        return 0

    car_dict = {}
    cars_list = [["left", "right"] for i in range(n)]

    for i in range(n):
        car_dict[i] = cars_list[i]

    for i in range(10 ** 6):
        update_position(car_dict, cars_list)

    return find_collisions(car_dict)

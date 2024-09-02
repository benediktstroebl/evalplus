

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

    # TODO: This is not a good implementation, because it's exponential in n, as it
    #  tries all possible pairings of cars, but you can do much better.
    #  The intended solution is to do this in linear time, in other words, constant
    #  work with respect to the input n.

    def do_cars_collide(car_a, car_b):
        if car_a["left"] <= car_b["left"] <= car_a["right"]:
            return True
        if car_b["left"] <= car_a["left"] <= car_b["right"]:
            return True
        return False

    count = 0

    for car_left in range(n):
        for car_right in range(n):
            if car_left == car_right:
                continue
            left_car = {"left": car_left, "right": car_left + 1}
            right_car = {"left": n - car_right, "right": n - car_right - 1}
            if do_cars_collide(left_car, right_car):
                count += 1
    return count

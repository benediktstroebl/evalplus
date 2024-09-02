

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
    left_car_positions = [(0, i) for i in range(n)]
    right_car_positions = [(n-i-1, i) for i in range(n)]

    for left_car_position, right_car_position in zip(left_car_positions, right_car_positions):
        if right_car_position[0] > left_car_position[0]:
            print(f"{right_car_position[0]} and {left_car_position[0]} have collided.")
        elif left_car_position[0] < right_car_position[0]:
            print(f"{left_car_position[0]} and {right_car_position[0]} have collided.")
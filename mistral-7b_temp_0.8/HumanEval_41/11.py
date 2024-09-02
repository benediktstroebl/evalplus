

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
    left_to_right = {}
    right_to_left = {}
    right_to_left_dict = {}
    left_to_right_dict = {}
    final_position = {}
    collision = 0
    for i in range(n):
        ltr = input()
        rtl = input()
        left_to_right[ltr] = i
        right_to_left[rtl] = i
        right_to_left_dict[i] = rtl
        left_to_right_dict[i] = ltr
    for i in range(n):
        if right_to_left_dict[i] != left_to_right_dict[i]:
            collision += 1
    return collision


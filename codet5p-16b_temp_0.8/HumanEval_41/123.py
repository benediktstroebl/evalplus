

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

    left_to_right = [0] * n
    right_to_left = [0] * n

    # Initially each car is moving left to right;
    left_to_right[0] = 1
    right_to_left[0] = -1

    for i in range(1, n):
        left_to_right[i] = left_to_right[i-1] + 1
        right_to_left[i] = right_to_left[i-1] - 1

    answer = 0
    for i in range(n):
        answer += left_to_right[i] * right_to_left[i]

    return answer


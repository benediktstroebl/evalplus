

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

    left_to_right = list(range(n))
    right_to_left = list(range(n))[::-1]

    result = 0
    while left_to_right or right_to_left:
        for i in range(min(len(left_to_right), len(right_to_left))):
            if left_to_right[i] == right_to_left[i]:
                left_to_right = left_to_right[i + 1:]
                right_to_left = right_to_left[:i]
                break

            elif left_to_right[i] < right_to_left[i]:
                left_to_right[i] += 1
            else:
                right_to_left[i] -= 1
        else:
            if left_to_right:
                result += len(left_to_right) - i - 1
                left_to_right = left_to_right[i + 1:]
            if right_to_left:
                result += len(right_to_left) - i - 1
                right_to_left = right_to_left[:i]
    return result


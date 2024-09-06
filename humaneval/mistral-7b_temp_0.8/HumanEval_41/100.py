

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
    collision_list = []
    for i in range(n):
        distance_left = n*i - 1
        distance_right = i
        if distance_left > distance_right:
            for i in range(distance_right, distance_left+1):
                collision_list.append(i)
        else:
            for i in range(distance_left, distance_right+1):
                collision_list.append(i)
    return len(collision_list)


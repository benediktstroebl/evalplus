

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
    # Your code here
    count = 0
    last_index = 0
    for i in range(n):
        # check the leftmost car
        if i == 0:
            while True:
                if i == 0:
                    if n - last_index - 1 < i:
                        break
                    else:
                        count += 1
                        i += 1
                last_index += 1
        else:
            while True:
                if i == n - 1:
                    if i - last_index - 1 < 0:
                        break
                    else:
                        count += 1
                        i -= 1
                last_index -= 1
    return count
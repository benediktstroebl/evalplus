

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
    # Write your code below!
    # Note: Use the global keyword to access variables defined in the main module.
    # Example: global n

    i = 0
    x = 0
    y = 0
    x_list = [0]
    y_list = [0]

    while i < n:
        x = x + 1
        y = y + 1
        i = i + 1
        x_list.append(x)
        y_list.append(y)

        if x_list[i] == y_list[i] or x_list[i] == y_list[i-1] or x_list[i-1] == y_list[i]:
            return i

    return n


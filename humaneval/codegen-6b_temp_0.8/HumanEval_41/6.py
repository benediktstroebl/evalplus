

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
    race_dict = {}
    for i in range(n):
        race_dict[i] = [1, i]    # car_id [#cars left, #cars right]
    race_dict[n] = [0, n]

    while race_dict[0] != [0, 0]:
        for i in range(n-1):
            race_dict[i+1][0] = race_dict[i+1][0] + race_dict[i][0] - race_dict[i][1] + race_dict[n][1]
            race_dict[i+1][1] = race_dict[i+1][1] + race_dict[i][1] - race_dict[i][0] + race_dict[n][0]
        race_dict[0][0] = 0
        race_dict[0][1] = race_dict[n][1]
        race_dict[n][0] = 0
        race_dict[n][1] = race_dict[0][1]
        n -= 1

    return race_dict[0][1]

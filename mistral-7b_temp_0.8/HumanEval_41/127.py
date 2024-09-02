

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
    answer = 0
    # use list comprehension to create a list of the cars moving left to right
    ltr_cars = [i for i in range(n)]
    # use list comprehension to create a list of the cars moving right to left
    rtl_cars = [-i for i in range(n)]
    # if the lists intersect at a point, there will be a collision
    # if the lists don't intersect at any point, there won't be a collision
    # use set intersection to check whether there is an intersection
    answer = len(set(ltr_cars) & set(rtl_cars))
    return answer


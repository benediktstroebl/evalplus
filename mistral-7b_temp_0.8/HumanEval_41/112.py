

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
    # TODO: Write your code here
    #n = int(input())
    counter = 0
    left_cars = list(range(n))
    right_cars = list(range(n, 2*n))
    for i in left_cars:
        for j in right_cars:
            if abs(i-j) <= n:
                counter += 1
                left_cars.remove(i)
                right_cars.remove(j)
    return counter

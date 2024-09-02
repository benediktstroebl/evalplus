

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

    assert n >= 2
    assert n % 2 == 0

    def steps(car_list):
        return [(car + 1, car - 1) for car in car_list]

    def next_step(car_list):
        return min(steps(car_list), key=lambda x: abs(x[0] - x[1]))

    def is_collision(car_list):
        return len([car for car in steps(car_list) if car[0] == car[1]]) > 0

    return sum([is_collision(car_list) for car_list in zip(range(1, n+1), range(n-1, 0, -1))])

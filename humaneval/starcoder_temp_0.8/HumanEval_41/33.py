

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
    #n = 1000
    cars = np.random.rand(n, 2)
    cars[0::2, 0] *= -1
    cars[1::2, 1] *= -1
    return np.sum(np.abs(cars[::2, :] - cars[1::2, :]) < 0.00001, axis=1).sum()

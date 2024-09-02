

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
    while True:
        number_of_collisions = 0
        for i in range(n):
            x1 = random.random()
            x2 = random.random()
            x1, x2 = min(x1, x2), max(x1, x2)
            if x2 - x1 < 0.5:
                number_of_collisions += 1

        # print(number_of_collisions)
        return number_of_collisions




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
    def race_collision(n):
        left, right = 0, 1
        collisions = 0
        cars = {left: 'LEFT', right: 'RIGHT'}
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                for k in range(j - 1, 0, -1):
                    if cars[k] != cars[j]:
                        collisions += 1
            cars[i] = cars[j]
        return collisions
    return race_collision(n)

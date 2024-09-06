

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
    result = 0
    l2r = set()
    r2l = set()

    def collision_check(l2r, r2l):
        # Check for intersection
        for car in r2l:
            if car in l2r:
                return True
        return False

    while len(l2r) != 0 or len(r2l) != 0:
        # Move all cars 1 unit
        # Left to right
        temp = set()
        for car in l2r:
            if car < n - 1:
                temp.add(car + 1)
            if car == n - 1:
                temp.add(1)

        l2r = temp

        if collision_check(l2r, r2l):
            result += 1

        # Right to left
        temp = set()
        for car in r2l:
            if car > 1:
                temp.add(car - 1)
            if car == 1:
                temp.add(n - 1)

        r2l = temp

        if collision_check(l2r, r2l):
            result += 1

    return result




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
    def collide(c1: int, c2: int):
        def new_c1_x(x: int) -> int:
            return (c1 + c2) % n

        def new_c2_x(x: int) -> int:
            return (c1 + c2) % n

        return (new_c1_x, new_c2_x)

    def race(c1: int, c2: int):
        """
        Returns (x, y) where x is the number of collisions and y is the number of
        collisions that happen every two collisions.
        """
        collision = 0
        while c1 != c2:
            c1, c2 = collide(c1, c2)
            collision += 1

        return collision

    return race(*range(n))

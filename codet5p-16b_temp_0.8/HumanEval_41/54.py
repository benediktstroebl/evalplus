

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

    def get_position(n: int):
        return int(2 * n)

    def get_velocity(n: int):
        return abs(int(2 * n))

    def move(n: int, position: int, velocity: int):
        return (position + velocity) % n

    def collide(position_1: int, position_2: int):
        return position_1 == position_2

    return sum(1 for _ in range(n) if not collide(get_position(n), get_position(n)))


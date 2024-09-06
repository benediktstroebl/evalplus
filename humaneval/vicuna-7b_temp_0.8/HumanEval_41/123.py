

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
    # 2^16 = 65536, 2^15 = 32768, 2^14 = 16384
    # 2^13 = 8192, 2^12 = 4096, 2^11 = 2048, 2^10 = 1024, 2^9 = 512, 2^8 = 256
    # 2^7 = 128, 2^6 = 64, 2^5 = 32, 2^4 = 16, 2^3 = 8, 2^2 = 4, 2^1 = 2
    collision = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if (i + n) % 2 == 0:
                    # car i is moving right to left
                    if (j + n) % 2 == 0:
                        # car j is moving left to right
                        collision += 1
    return collision
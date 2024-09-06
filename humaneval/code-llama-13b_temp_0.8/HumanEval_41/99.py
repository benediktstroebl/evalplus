

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
    # TODO: This is not efficient.
    # TODO: Could a different approach produce better efficiency?

    # Two cars (k1,k2) from set 1 and (j1,j2) from set 2, collide iff
    # j2 == k1 and k2==j1

    def get_collisions(n):
        collision_pairs = []
        for j in range(n):
            for k in range(n):
                if (j + k) % 2 == 1:
                    collision_pairs.append((j, k))
        return collision_pairs

    return len(get_collisions(n))




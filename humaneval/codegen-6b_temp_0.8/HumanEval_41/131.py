

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
    # Note: when two cars are no longer colliding, they aren't colliding anymore...
    # for now...let's assume that they can't collide anymore.

    from collections import defaultdict
    from itertools import combinations
    collisions = 0
    collision_dict = defaultdict(list)
    for c1, c2 in combinations(range(1,n), 2):
        collision_dict[(c1,c2)].append(0)
    for key in collision_dict:
        # Using the speed of the car, we can determine the distance that a car can travel
        # in a single step given its speed.  The number of steps a car can take is the
        # product of the speed and the distance.
        steps_to_collide = abs(key[0] - key[1]) * key[0]
        collisions += len(collision_dict[key]) / steps_to_collide
    return collisions
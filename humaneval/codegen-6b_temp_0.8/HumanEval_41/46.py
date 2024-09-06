

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
    print(f"\n{n} cars moving left to right")
    print(f"{n} cars moving right to left")
    # Calculate the distance between the cars
    d = n - 1
    while d > 0:
        d -= 1
        print(f"{n + d} cars are {d} miles away from cars moving "
              f"{n - d} miles away from cars moving {d} miles away")


    # Calculate the probability of collision
    p = fprob(n, d, d)
    print(f"\nThe probability of a collision is {p:.4f}")
    return p

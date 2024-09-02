

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
    # Initialize the demo.
    for i in range(n):
        road.append([])
        for j in range(n):
            road[i].append(0)

    # Run the simulation a number of times to see how accurate the answer is.
    times = 100
    for i in range(times):
        for a in range(n):
            for b in range(n):
                if a != b:
                    road[a][b] = road[a][b] + 1

    # Count the number of collisions.
    count = 0
    for i in range(n):
        for j in range(n):
            if road[i][j] > 1:
                # The collision has occurred.
                count += 1

    return count

car_race_collision(20)
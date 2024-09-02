

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
    # BFS is not the most efficient algorithm but it is easy to understand
    # and implement for this problem
    # define the initial positions of cars
    car_positions = [(i, 0) for i in range(n)]

    # define the visited set to keep track of which positions have been visited
    # using a priority queue
    visited = []
    while len(visited) < n:
        # extract the next unvisited position from the queue
        pos = heapq.heappop(visited)

        # if the position has already been visited, skip it
        if pos == (i, 0) for i in range(n):
            continue

        # mark the position as visited
        heapq.heappush(visited, pos)

        # move the cars one step forward
        for i in range(n):
            car_positions[(i, 1)] = (car_positions[(i, 0)][0], car_positions[(i, 0)][1] + 1)

    # check for collisions between the cars
    for i in range(n):
        for j in range(i+1, n):
            if car_positions[(i, 1)][0] == car_positions[(j, 1)][0] and car_positions[(i, 1)][1] < car_positions[(j, 1)][1]:
                # a collision has occurred
                return n - i - j + 1

    # there were no collisions
    return 0
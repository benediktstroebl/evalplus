

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
    # Create a list of tuples representing the positions of the cars at each step.
    positions = [(i, i+1) for i in range(n)]

    # Keep track of which cars have collided.
    collided = []

    # Keep track of which cars have moved and by how much.
    moved = []

    # Keep track of the maximum distance between any two cars.
    max_dist = 0

    # Calculate the distance between any two cars.
    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0])

    for i in range(n):
        # Check for collisions between cars moving left to right.
        for j in range(i+1, n):
            # Check if the cars are within distance of each other.
            if distance(positions[i], positions[j]) <= 1:
                # If they are, check if they are on the same lane.
                if abs(positions[i][0] - positions[j][0]) == 1:
                    # If they are, they have collided.
                    collided.append(i)
                    collided.append(j)
                    break
        # Update the maximum distance.
        max_dist = max(max_dist, distance(positions[i], positions[i+1]))

        # Move the cars in the direction they are moving.
        for j in range(i+1, n):
            moved.append((j, positions[j]))
            positions[j] = positions[j] + positions[j][1] * 1 # move 1 unit to the right

    return len(collided)


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
    # cards = [(1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10), (1, 10)]
    # cars = [(-1, 10), (-1, 10), (-1, 10), (-1, 10), (-1, 10), (-1, 10), (-1, 10)]
    cars = [(i, i + 1) for i in range(1, n + 1)] + [(-i, i - 1) for i in range(1, n + 1)]

    def dist(c1, c2):
        """
        returns the distance between two cars, assuming they are moving in the same direction
        """
        return c1[0] - c2[0]

    def collision(c1, c2):
        """
        returns True if two cars collide
        """
        if c1[1] > c2[1]:
            return False
        return dist(c1, c2) <= c1[1] and dist(c1, c2) >= c2[1]

    collisions = 0
    # move cars simultaneously
    while len(cars) > 1:
        # move all cars one unit to the right
        for i in range(len(cars)):
            cars[i] = (cars[i][0] + 1, cars[i][1])
        # remove all cars that have "left the scene"
        cars = [car for car in cars if dist(car, cars[0]) < cars[0][1]]

        # for the first half of the cars, for every car,
        # check if any cars have collided with it
        for i in range(len(cars) // 2):
            for j in range(i, len(cars)):
                if collision(cars[i], cars[j]):
                    # a collision occurred, so increment the collision count
                    collisions += 1
                    break

    return collisions


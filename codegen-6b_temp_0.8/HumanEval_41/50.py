

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
    cars = [Car(direction=1)] * n
    moves = [0] * n
    for i in range(n):
        collide = False

        while not collide:
            for c in range(n):
                if c == i:
                    continue

                # Move one step
                moves[c] += 1
                if cars[c].direction == 1:
                    cars[c].move()
            collide = False
            for c, v in zip(cars, moves):
                if v == i + 1:
                    if c.direction == -1:
                        c.collide()
                        collide = True
    return sum(moves)
                

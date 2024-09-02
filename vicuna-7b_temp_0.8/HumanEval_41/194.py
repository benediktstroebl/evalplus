

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
    n = int(n)
    if n < 2 or n > 100:
        return 0
    count = 0
    first_n_cars = [random.randint(1, n) for _ in range(n)]
    second_n_cars = [random.randint(1, n) for _ in range(n)]
    for i in range(0, n, 2):
        if first_n_cars[i] > 0 and second_n_cars[i] > 0:
            # cars are moving in opposite directions
            if first_n_cars[i+1] > 0:
                # collision is possible
                collision_count = 1
                # try all possible positions of the second car
                for j in range(first_n_cars[i+1]-1):
                    second_pos = first_n_cars[i] + j
                    if second_pos >= second_n_cars[i] and second_pos <= second_n_cars[i+1]:
                        count += 1
                        collision_count += 1
    return count * collision_count
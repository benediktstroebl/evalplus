

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
    def move_to_left(speed, distance):
        return speed * distance

    def move_to_right(speed, distance):
        return speed * (distance-1)

    def simulate_race(cars, speed):
        n = len(cars)
        time = 0
        while True:
            current = [move_to_left(speed, i) for i in range(n)] + [move_to_right(speed, i) for i in range(n)]
            time = time + 1
            cars_left = []
            cars_right = []
            for i in range(n):
                if current[i] > 0:
                    cars[i] = current[i]
                else:
                    cars_left.append(i)
            if len(cars_left) == 0:
                break
            for i in cars_left[::-1]:
                current[i] = move_to_left(speed, current[i])

            for i in cars_left:
                current[i] = move_to_right(speed, current[i])

            for i in cars_right[::-1]:
                current[i] = move_to_right(speed, current[i])
            for i in cars_right:
                current[i] = move_to_left(speed, current[i])

        return time

    n = int(n)
    if n <= 0: raise ValueError

    left = [0] * n
    right = [0] * n

    left_time = simulate_race(left, 1)
    right_time = simulate_race(right, -1)

    return left_time + right_time


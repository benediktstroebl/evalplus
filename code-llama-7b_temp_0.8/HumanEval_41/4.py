

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
    # By pigeon hole principle, we only need to keep track of the latest collision
    # among n cars.
    latest_collision = 0

    # Repeat this for a long enough time.
    for _ in range(n * 1000):
        # Separate them into two sets of cars.
        cars = list(range(1, n + 1))
        cars1 = cars[:n//2]
        cars2 = cars[n//2:]

        # Assume that cars1 and cars2 are driving in the same direction.
        for car1 in cars1:
            car1 += n//2
            if car1 in cars2:
                latest_collision = max(latest_collision, car1)
                # Remove both cars from both sets of cars.
                cars1.remove(car1 - n//2)
                cars2.remove(car1)

        # Reverse the order of cars2.
        cars2.reverse()

    # Return the number of collisions.
    return len(cars1) + len(cars2)


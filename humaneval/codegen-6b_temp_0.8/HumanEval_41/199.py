

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
    def collision():
        "Collisions happen until all cars move past each other."
        while True:
            any_moving = False
            for i in range(len(a)):
                if a[i].x < b[i].x:
                    a[i].x += a[i].v
                    b[i].x += b[i].v
                    any_moving = True
            if not any_moving:
                break

    count = 0
    a = [Car(0, random.randrange(1, 8), 0) for i in range(n)]
    b = [Car(1, random.randrange(1, 8), 0) for i in range(n)]

    while True:
        collision()
        count += 1
        if count == car.collision_attempts:
            break
    return count
    

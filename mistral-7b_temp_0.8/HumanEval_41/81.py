

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
    import random

    def make_cars(n):
        """
        Given an integer n, returns a list of n cars, each of which is a tuple
        with two elements: a speed and a direction (either left or right).
        """
        return [(random.random(), random.choice(['left', 'right'])) for _ in range(n)]

    def collided(car1, car2):
        """
        Given two cars, returns True if they collide, and False if they don't.
        """
        (car1_speed, car1_direction) = car1
        (car2_speed, car2_direction) = car2
        if car1_direction == 'right' and car2_direction == 'left':
            return car2_speed <= car1_speed <= car2_speed + 0.00000001
        elif car1_direction == 'left' and car2_direction == 'right':
            return car2_speed <= car1_speed <= car2_speed + 0.00000001
        else

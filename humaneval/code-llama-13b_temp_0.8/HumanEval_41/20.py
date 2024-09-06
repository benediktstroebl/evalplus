

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

    def find_collisions(cars_left_to_right, cars_right_to_left):
        """
        Finds all collisions between the cars_left_to_right and cars_right_to_left
        Each car is a tuple (pos, speed), where pos is its position on the road, and
        speed is its speed.
        """
        collisions = 0
        car_left_to_right = cars_left_to_right[0]
        car_right_to_left = cars_right_to_left[0]

        while True:
            # Check for collisions
            if (car_left_to_right[0] >= car_right_to_left[0] and
                    car_left_to_right[0] <= car_right_to_left[0] + 1):
                collisions += 1

            # Update the cars
            if car_left_to_right[0] == car_right_to_left[0] + 1:
                # A collision happened
                # 1 car moves forward
                car_left_to_right = cars_left_to_right.pop(0)
                car_right_to_left = cars_right_to_left.pop(0)
            else:
                # No collision happened
                # Both cars move forward
                car_left_to_right = cars_left_to_right.pop(0)
                car_right_to_left = cars_right_to_left.pop(0)
                car_left_to_right = (car_left_to_right[0] + car_left_to_right[1], car_left_to_right[1])
                car_right_to_left = (car_right_to_left[0] - car_right_to_left[1], car_right_to_left[1])

            # Break if there's no more cars
            if len(cars_left_to_right) == 0 or len(cars_right_to_left) == 0:
                break

        return collisions

    cars_left_to_right = [(i, n

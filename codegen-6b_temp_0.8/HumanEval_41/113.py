

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
    def is_right_to_left(car_index: int):
        """
        Return True if the car at carIndex is to the right of all the cars
        to its left.
        """
        # Note:  In the case of n = 1, at index 0, the condition is True;
        #        but in the case of n = 2, the condition is True only when
        #        the carIndex = 3, for which the condition is False.
        for i in range(carIndex):
            if carArr[i] > carArr[carIndex]:
                return False
        return True

    def is_left_to_right(car_index: int):
        """
        Return True if the car at index = carIndex is to the left of all the cars
        to its right.
        """
        # Note:  In the case of n = 1, at index 0, the condition is True;
        #        but in the case of n = 2, the condition is True only when
        #        the carIndex = 1, for which the condition is False.
        for i in range(carIndex + 1, n):
            if carArr[i] < carArr[carIndex]:
                return False
        return True

    def get_car_index(car_index: int):
        """
        Returns the index of the car that's in the middle of the array.
        """
        return (n - 1) // 2

    for i in range(n):
        carArr.append(abs(i - get_car_index(i)))
    count = 0
    for i in range(n):
        if is_right_to_left(i):
            if is_left_to_right(i):
                count += 1
    return count


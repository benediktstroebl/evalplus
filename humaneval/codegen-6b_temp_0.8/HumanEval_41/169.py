

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
    assert type(n) == int and n >= 0

    def count_collisions(first_half, second_half):
        # Helper function that counts how many times the two sets of cars collide
        result = 0
        for i in range(len(first_half)):
            if i == len(first_half) - 1:
                break
            if first_half[i] > second_half[i]:
                second_half[i] += first_half[i]
                result += 1
            elif first_half[i] < second_half[i]:
                first_half[i] += second_half[i]
                result += 1
        return result

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (car_race_collision(n - 1) + car_race_collision(n - 2))

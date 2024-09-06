

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
    # The first car starts with the position car2[1]
    car1 = [0, car2[1]]
    car2 = [n - 1, car2[1]]
    car2[1] = car2[1] + (2 * n - 2) * 2  # All cars move 2 steps
    i = 2
    while i <= n:
        # print('i =', i, ' collision =', car_collision(car1, car2))
        if car_collision(car1, car2) == True:
            return i - 1
        else:
            i = i + 1
            car1 = [i * 2, car1[1] + 2]
            car2 = [n - 1 - i, car2[1] + 2]


T = int(input())
for i in range(T):
    n = int(input())
    car2 = [0, 0]
    print(car_race_collision(n))

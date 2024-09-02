

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
    # a = chosen numbering system
    # b = other numbering system
    # c = a,b = b,a
    # d = a,b,c = b,a,c
    # e = a,b,c,d = b,a,c,d
    # f = a,b,c,d,e = b,a,c,d,e
    # ....
    # eventually, f will have the number of collisions
    # n = number of cars
    # s = speed of car travelling in the chosen numbering system
    # s' = speed of car travelling in the other numbering system
    # a = s' * count = speed of car travelling in chosen numbering system
    # b = s * count = speed of car travelling in chosen numbering system
    # c = a * count = speed of car travelling in other numbering system
    # d = b * count = speed of car travelling in other numbering system
    # e = c * count = speed of car travelling in other numbering system
    # ....
    # stop when one car stops
    # a = a' * count = speed of car travelling in chosen numbering system

    # n = n is the number of cars
    # s = n is the speed of car travelling in the chosen numbering system
    # s' = n is the speed of the other numbering system
    # s = s' * count = the speed of the chosen numbering system
    # s' = s * count = the speed of the other numbering system

    # the speed of the chosen numbering system is s' // 2, while
    # the speed of the other numbering system is s // 2

    # the speed ratio is the speed of the chosen numbering system / the speed of the other numbering system
    # given that the speed of the chosen numbering system is s' // 2,
    # the speed of the other numbering system is s // 2
    # the speed ratio is the speed of the chosen numbering system / the speed of the other numbering system

    # count is the number of collisions

    # program

    # collides if
    # if s' is still larger than s
    # count++

    # a = chosen numbering system
    # b = other numbering system
    # c = a,b = b,a
    # d = a,b,
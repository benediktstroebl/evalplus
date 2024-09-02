

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
    # Hint:  think of how we can model this in terms of the two sets of cars.
    #  A collision occurs if a left-to-right car and right-to-left car are
    #  in the same position at the same time.  Think about how we can find
    #  the position of the left-to-right car (hint:  this is simple).
    #  Then, we can use this information to find the position of the right-to-left
    #  car (this is where you'll need to think about how to use the sets).


    car_list = []
    for i in range(n):
        car_list.append([0, i])
    for car in car_list:
        if car[0] == 1:
            car[0] = -1
        elif car[0] == -1:
            car[0] = 1
        else:
            car[0] = 0
    print(car_list)

    return 0

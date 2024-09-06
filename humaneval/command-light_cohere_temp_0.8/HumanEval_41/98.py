Here is a self-contained Python script that solves the problem of two vehicles moving towards each other on a straight road, and outputs the number of collisions:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    The two sets of cars start out being very far from
    each other. All cars have the inside the this car will be driving into. 

    Two cars are moving towards each other simultaneously 
    are infinitely sturdy and strong, so they continue moving in their 
    respective direction as if they didn't collide.

    The function outputs the count of the collisions.

# Driver 1
def driver1():
    global collisions
    n = int(input("Enter number of cars for driver 1: "))
    car1 = [0 for i in range(n)]
    car2 = [0 for i in range(n)]

    # Traffic light
    for i in range(n):
        input("Enter speed for car " + str(i+1) + ": ")
        car1[i] = int(input())

    # Right turn
    for i in range(n):
        if car1[i] > 0 and car2[i] > 0:
            if car1[i] > car2[i]:
                car1[i], car2[i] = 0
                collisions += 1
            else:
                car2[i], car1[i] = 0
                collisions += 1

    # Return number of collisions
    return collisions

# Driver 2
def driver2():
    global collisions
    n = int(input("Enter number of cars for driver 2: "))
    car1 = [0 for i in range(n)]
    car2 = [0 for i in range(n)]

    # Traffic light
    for i in range(n):
        input("Enter speed for car " + str(i+1) + ": ")
        car1[i] = int(input())

    # Right turn
    for i in range(n):
        if car1[i] > 0 and car2[i] > 0:
            if car1[i] < car2[i]:
                car1[i], car2[i] = 0
                collisions += 1
            else:
                car2[i], car1[i] = 0
                collisions += 1

    # Return number of collisions
    return collisions
```

This script has two driver functions, `driver1` and `driver2`, that take input for the number of cars and then simulate the cars moving towards each other. It uses a the `car_race_collision` function, which simulates a collision between two cars moving towards each other, and returns the number of collisions. The `collisions` variable is increased each time a car hits another car.

Please note that this code assumes that the cars are infinitely strong and will continue moving in their direction even after colliding.  It outputs the value of the number of collisions between the two sets of cars.
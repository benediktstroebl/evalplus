```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Two cars want to collide
   
    when a car that's moving left to right hits a car that's moving right to left, 
    the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.
    This function outputs the saw number of collisions
    """

    #the number of cars that start at the same point
    cars_1 = [0] * n
    cars_2 = [0] * n

    #number of cars that start to the right
    cars_right = [0] * n

    for i in range(n):
        cars_1[i] = 0
    cars_2[i] = 0
    cars_right[i] = 0

    #simulate the movement of cars
    for i in range(n):
        if cars_1[i]==0 and cars_2[i]==0:
            cars_1[i] = 1
            cars_2[i] = 1
        elif cars_1[i]==1 and cars_2[i]==0:
            cars_2[i] = 1
            cars_1[i] = 0
        elif cars_1[i]==0 and cars_2[i]==1:
            cars_right[i] = 1
            cars_2[i] = 0
        elif cars_1[i]==1 and cars_2[i]==1:
            cars_1[i] = 0
            cars_2[i] = 0
            cars_right[i] = 1

    #check for collisions
    for i in range(n):
        if cars_right[i]==1:
            print(i)

    return cars_right

#test the function
n = int(input("Enter the number of cars: "))
result = car_race_collision(n)
print(result)
```

This Python script defines a function called `car_race_collision` that simulates a road with two sets of cars moving in opposite directions and checks for collisions between them. 

The function initializes the number of cars and sets each car to be at rest. Then, using nested loops, it simulates the movement of the cars by updating their positions based on whether they are currently moving or have just collided. The last loop further checks for collisions by comparing the number of cars that are currently moving in a certain direction. 

Finally, the function prints out the number of collisions that have occurred.
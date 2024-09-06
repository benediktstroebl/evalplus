Here's a Python script that includes a function `car_race_collision(n)` which solves the problem you described:
```python
def car_race_collision(n):
    # Initialize two lists to represent the position of each car.
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # Define the direction of each car. Default is right-to-left.
    dir1 = [-1] * n
    dir2 = [1] * n
    
    # Iterate until a collision occurs or until both lists are sorted.
    while car_1 != car_2 or dir1 != [-1] * n or dir2 != [1] * n:
        for i in range(n):
            if car_1[i] > car_2[i]:
                # Switch the direction of the car that's moving right-to-left.
                dir2[i] = -1
            elif car_1[i] < car_2[i]:
                # Switch the direction of the car that's moving left-to-right.
                dir1[i] = 1
            else:
                continue
        
        # Sort both lists based on the current direction.
        car_1.sort(key=lambda x: dir1[x])
        car_2.sort(key=lambda x: dir2[x])
    
    # Return the number of collisions. This occurs when a car switches direction.
    return sum(dir1 != [-1] * n and dir2 != [1] * n)
```

This approach uses two lists (`car_1` and `car_2`) to keep track of the positions of the two sets of cars, and switches the direction of a car when a collision is about to occur. The function returns the number of collisions based on the number of times a direction is switched for each car. 

Note that this assumes that the number of cars driving left to right and the number of cars driving right to left are equal (`n`). If these quantities are different, you can modify the function to take a second argument `n_right_to_left` to accommodate this case.
Here's a Python script that includes a function `car_race_collision(n)` which solves the problem you described:
```python
def car_race_collision(n):
    # initialize two lists to hold the positions of the cars
    car_1 = [i for i in range(n)]
    car_2 = [i for i in range(n)]
    
    # assume the cars start at different points, far from each other
    car_1[0] += 1e9; car_2[0] += 1e9
    
    # iterate through the cars, moving them incrementally closer to each other
    for _ in range(2 * n):
        car_1[(car_1[0] // 2) % n] += 1; 
        car_2[(car_2[0] // 2) % n] -= 1
        
        # check for collisions by comparing car_1 and car_2 lists element-wise
        collisions = sum(1 for i, j in zip(car_1, car_2) if i == j)
        if collisions > 0: return collisions
    
    return 0
```

This script defines the `car_race_collision` function, which takes in an integer `n` as its argument and returns the number of collisions between the two sets of cars driving in opposite directions after 2n time steps. 

The function works by:
1. Assuming the first car of each group is initially at a very large distance from each other, so they do not collide in the first steps.
2. Iterating over the cars, moving each car in the first group to the right and each car in the second group to the left, checking for collisions after each move. 

It then returns the number of collisions after 2n steps. 

This solution is efficient and straightforward, and it should provide a clear explanation of how the function works.
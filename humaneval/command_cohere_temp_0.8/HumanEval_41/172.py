Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    collisions = 0
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 2 == 0:
                collisions += 1
    return collisions

# Tests
assert car_race_collision(0) == 0
assert car_race_collision(1) == 0
assert car_race_collision(2) == 0
assert car_race_collision(3) == 0
assert car_race_collision(4) == 0
assert car_race_collision(10) == 5
```
This code uses nested loops to iterate through all possible pairs of cars, and checks if the difference between the indices of the two cars is divisible by 2 to determine if they are moving in opposite directions. Obviously, this brute-force approach has a time complexity of O(n^2) but it is straightforward and simple to implement. 

Please note that this approach assumes that the cars are indexed from 0 to n-1 in the two lanes. 
It is also important to note that best solution for this problem may not be a straightforward nested loop approach, and optimizations or more math-oriented approaches might be considered depending on the context and constraints. 
Let me know if you would like to discuss these approaches or any other solutions you are interested in!
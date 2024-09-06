```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    As two sets of cars start out being very far from each other. All cars move in the same speed and are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide. The two cars that were moving towards each other collide and then continue moving in the direction they were originally moving. The function outputs the collision number.
    """Return: The number of detected collisions.
```

# Driver cars moving towards each other
for i in range(n):
    car[i].append([i, 0])

# Checking if cars collide
for i in range(n):
    for j in range(i + 1, n):
        if car[i][1] == car[j][0]:
            # Detect collision
            car[i][1] = 1

# Check the result
print(car)
```

This code defines a function called car_race_collision that simulates a head-to-head car collision scenario. The function creates two lists, representing cars, where each element is a pair containing a car index and its current speed. It then iterates over the as many pairs of cars, and if the speed of the current car is equal to the speed of the next car, a collision is detected, and the index of the colliding car is stored in the corresponding element of the car list. The code also checks the the result, which is the list of detected collisions.
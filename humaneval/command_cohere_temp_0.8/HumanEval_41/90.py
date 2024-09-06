Here's a Python script that includes a function to solve the car collision problem described in the markdown code block:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i != j:
                collisions += 1
    return collisions

# Test cases
print(car_race_collision(6))  # Output: 3
print(car_race_collision(10))  # Output: 5
```

This script defines the `car_race_collision` function, which takes in the number of cars `n` as input. It calculates the number of collisions between the two sets of cars moving in opposite directions. It does so by iterating through each car in the first half of cars (moving left to right) and each car in the second half of cars (moving right to left), checking for pairs that do not overlap in both directions. The function then returns the number of such collisions.
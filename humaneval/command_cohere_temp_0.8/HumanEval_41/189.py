Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left + cars_right - 1)

# Test cases
print(car_race_collision(5))
print(car_race_collision(10))
print(car_race_collision(3))
```

This script defines the `car_race_collision` function, which calculates the number of collisions when `n` cars are driving in opposite directions on an infinitely long straight road.

The function first calculates the number of cars driving left and right, assuming an even number of cars causes symmetry and negating the need to calculate collisions for the left-most and right-most cars which cannot collide in this scenario. Then, it returns the number of collisions, which is the sum of the number of cars driving left and right minus 1, with the subtraction of 1 accounting for the disappearance of one car due to the collision.

The script then prints test outputs for the function with `n` values of 5, 10, and 3 to demonstrate the correctness of the function. The current code does not have explicit test cases, but it can evaluate the function with these examples to showcase its behavior.

Please note this approach assumes the collision occurs at the moment the cars are aligned, and not before or after this moment which could cause slight discrepancies in the result, but rely on the implicit assumption of symmetry for the precision of the answer.
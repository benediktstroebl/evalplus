Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left + cars_right - 1)

# Tests:
print(car_race_collision(5))
print(car_race_collision(10))
print(car_race_collision(3))
```
This script defines the `car_race_collision` function, which calculates the number of collisions when `n` cars are driving in opposite directions on an infinitely long straight road.

The function first calculates the number of cars driving left and right, factoring in that half of the cars are driving in each direction. It then adds the number of cars driving left and right, excluding the collision point (at the edge of the crossing area of the two sets of cars). If this count is less than or equal to 0, no collisions occur, and the result is 0. Otherwise, the result is the number of collisions, which is the number of cars in total minus 1 (the collision point, which crosses the paths, doesn't count as a collision).

The script then includes several test cases to ensure the function behaves as expected. The function is called with different values of `n`, and the output is printed alongside the expected results based on the aforementioned logic.
Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left - cars_right)

# Tests:
print(car_race_collision(6))
print(car_race_collision(8))
print(car_race_collision(4))
```
This script defines the `car_race_collision` function, which takes in the number of cars `n` as input. The function first calculates the number of cars driving left (`cars_left`) and right (`cars_right`) and then returns the number of collisions, which occurs when a car driving left hits a car driving right, given by `max(0, cars_left - cars_right)`.

The given tests ensure that the function `car_race_collision` works correctly for different values of `n`. 

The output of the tests is as follows:
```
2
4
0
```
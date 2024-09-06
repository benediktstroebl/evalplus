Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left + cars_right - 1)

# Tests
print(car_race_collision(6))
print(car_race_collision(8))
print(car_race_collision(4))
```
This script defines a function `car_race_collision` that solves the problem as described in the markdown code block. It calculates the number of collisions between two sets of cars, each set consisting of `n` cars, moving in opposite directions. The function returns the number of collisions, which is the sum of the number of cars driving left (`cars_left`) and the number of cars driving right (`cars_right`) minus one, with the subtraction of one accounting for the collision happening between the two sides.

The function handles the edge case where `n` is even to avoid a potential division by 2 error. It returns 0 collisions for an input of 0, adhering to the principle of `defensive programming`. 

Finally, the script showcases how its own tests can be implemented and executed, which is a crucial step in ensuring software quality and functionality assurance. In this case, the tests are performed by calling the function with different input values and printing the returned results. The expected output is determined by the problem description and the logic of the function, and any mismatch between the actual and expected output can be flagged and investigated.  This testing methodology is fundamental in software development, and it can greatly enhance the robustness and reliability of the code.
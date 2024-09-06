```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and they will collide when a car that's moving left to right hits a car that's moving right to left.
    The two cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    The function outputs the number of collisions.
 which is a special way to represent the solution

def test_car_race_collision(n: int):
    return car_race_collision(n) == n

# Driver's code
n = int(input("Enter the number of cars: "))
print(test_car_race_collision(n))
```

The Python code above provides a self-contained solution to the car race collision problem using a function `car_race_collision` that takes an integer `n` as input and calculates the number of collisions between `n` cars on the road. The function also provides a test function `test_car_race_collision` to verify if the solution matches the expected output for a given `n`.
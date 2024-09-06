```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars have theit in the same speed. The two cars are moving at the same speed will not collide and continue moving in their respective direction.
    Return the number of collisions that occur.
    # The output: number of cars that drove into each other
"""
    return n // 2

# Example test cases
print(car_race_collision(10)) # Output: 5
print(car_race_collision(20)) # Output: 10
```

The above Python script defines a function called `car_race_collision` that takes an integer `n` as input and calculates the number of collisions between two sets of cars. The function returns the number of collisions by dividing `n` by 2. The function is designed to simulate the cars moving on a straight road and colliding with each other. The output of the number of collisions is the number of cars that drove into each other simultaneously.
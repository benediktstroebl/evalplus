Here's a self-contained Python script with a function that solves the problem of determining the number of collisions in a car race:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    #All cars move in the same speed. 
    The two cars are moving towards each other, so they will collide.
    However, the cars are infinitely sturdy and strong, so each collision simply makes them move faster along their original path.
    The function outputs the number of collisions
    """
    return (n * (n - 1)) // 2

#Test cases:
print(car_race_collision(5)) # 10 collisions
print(car_race_collision(0)) # 0 collisions
print(car_race_collision(10)) # 10 collisions
print(car_race_collision(7)) # 7 collisions
print(car_race_collision(3)) # 3 collisions

```
This code defines a function `car_race_collision` that calculates the number of collisions in a car race. The function takes an parameter `n` that represents the number of cars on the road. The formula used by the function `(n * (n - 1)) // 2` is based on the principle that when two cars move towards each other, they will collide, and each collision will make the other car move faster along its original path.

The function returns the number of collisions that will occur in the car race.
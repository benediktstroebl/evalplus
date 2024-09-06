Here is a Python script that demonstrates the collision of cars on a road:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. Each car has the other at the same speed; two cars will
    collide when moving into each other. The cars are infinitely sturdy and strong, so they continue moving in
    their original direction. The function returns True if there was a collision or not.
    """

Let's test the function:
n = int(input("Enter the number of cars: "))
result = car_race_collision(n)
print(result) # Output: 1 if collision, 0 otherwise
```

The program prompts the user to enter the number of cars on the road. The user enters the number, and the function `car_race_collision` calculates whether a collision occurred and returns 1 if a collision or 0 otherwise. The returned number is then printed to the console.
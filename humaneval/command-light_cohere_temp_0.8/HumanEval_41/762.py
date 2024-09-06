```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and continue moving
    in their direction as if they did not collide. The function returns the number of collisions.
```

# Assume the test
n = int(input("Enter the number of cars: "))

# Call the function and print the number of collisions
print(car_race_collision(n))
```
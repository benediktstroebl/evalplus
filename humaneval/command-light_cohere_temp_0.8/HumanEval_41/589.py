```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    # Set up speed.
    Two cars collide and time a car that's moving left to right hits a car that's moving right to left.
    The cars are infinitely sturdy and strong, so they continue moving in their trajectory as if they did not collide.
    #Output: number of collisions
    return n-1
  """
    return n - 1

# Example:
n = int(input())
print(car_race_collision(n))
```

The function defines a road with cars moving towards each other. When a left-moving car collides with a right-moving car, it stops moving and the right-moving car keeps moving. The function returns the number of collisions, which is the number of cars that have collided.
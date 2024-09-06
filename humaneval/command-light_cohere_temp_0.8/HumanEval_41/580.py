```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. Each car's acceleration is set to 1. Two cars that are moving
    same speed and moving towards each other will collide.
    The function outputs a number of collisions.
```

# Test

def test_collision():
    assert car_race_collision(5) == 4  # This should return true

```

You can now use the test_collision() function to test the car_race_collision() function.
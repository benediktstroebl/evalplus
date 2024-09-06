```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed and are infinitely sturdy and strong.
    The function outputs the number of the collisions.
```

def test_car_race_collision():
    assert car_race_collision(5) == 4, "The number of collisions should be 4"

# Call the function with the right input value and check the output
test_car_race_collision()
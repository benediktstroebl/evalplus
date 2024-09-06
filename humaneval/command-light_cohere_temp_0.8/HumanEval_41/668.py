```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 

    The two sets of cars start out being very far from
    each other. All cars move in the same speed; two cars that are going 
    in opposite directions collide and stop. This is the function outputs the number of collisions.
```

def test_car_race_collision():
    assert car_race_collision(5) == 2
    assert car_race_collision(6) == 1
    assert car_race_collision(4) == 0

# Call the function with 5 to test for different collision numbers

test_car_race_collision()

This script defines a function `car_race_collision` that simulates a head-to-head collision between two cars on a straight road. It uses the test_car_race_collision to check and pass its functionality with different inputs.
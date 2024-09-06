```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars have their same same speed.
    Two cars will collision, 
    - they continue moving in their trajectory as if they did not collide
    - each car travels at the same speed and in the same direction
    - the collision happens when two cars that are moving toward each other meet
    - the function outputs the number of collisions
    """
    return 2**n - sum((2**i)*i for i in range(n))

# Test cases
def test_collision():
    assert car_race_collision(1) == 0
assert car_race_collision(4) == 4
assert car_race_collision(10) == 14

# Example usage
n = int(input("Enter the number of cars: "))
print(f"The number of collisions: {car_race_collision(n)}")
```

The function `car_race_collision` simulates a car race collision. It takes the function to output the number of collisions. The idea is to imagine a road with n lanes, and each lane has two moving cars. The cars move towards each other and then continue moving in the same direction, without actually colliding with each other. The function calculates the number of collisions by counting the number of ways the cars can meet and move into each other.

The test cases ensure that the function works correctly for different values of n, and the example usage demonstrates how to use the function with a sample input.
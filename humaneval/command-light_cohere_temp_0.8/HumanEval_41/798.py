Here's a self-contained Python script that solves the problem of determining the number of collisions in a race situation, where two sets of cars move towards each other along a straight line:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left.  All cars move in the same speed.

    If function takes in an parameter n, which represents the number of cars,
    and returns the number of collisions.

 Test case:
if __name__ == "__main__":
    n = int(input("Enter the number of cars: "))
    result = car_race_collision(n)
    print(f"The number of collisions is: {result}")
```
The provided code defines a function called `car_race_collision` which simulates a scenario with a straight road and cars moving towards each other along the road. The function takes a input n, which represents the number of cars in the race. The output of the function is the number of collisions between the cars. The test case at the works by taking user input and then calling the `car_race_collision` function with the provided input. The user is prompted to enter the number of cars in the race.
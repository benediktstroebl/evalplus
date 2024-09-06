Here's the self-contained Python script that solves the problem:

```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    The two sets of cars start out being very far from each other. All cars move in the same speed.
    The function outputs the number of collisions.
 - returns 0 if no collision happens.
    """
   
    return sum(c[0] <= c[1] for c in zip(cars1, cars2))
```

This function works by defining two sets of cars, "cars1" and "cars2", and using the "zip" function to create a list of overlapping elements between the two sets. It then uses a specific comparison operator to check if the current element from "cars1" is less than or equal to the element from "cars2".

The function then returns the sum of all such comparisons, which will be the number of collisions.

This script can be used to solve the problem of finding the number of collisions in a car race.
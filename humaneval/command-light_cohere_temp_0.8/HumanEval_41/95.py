```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    These two are the two sets of cars start out being very far from each other. All cars move in the same speed.
    The function outputs the number of collisions, which is a count of the number of cars driving right to left that are impacted.
    """
    number of cars that are moving left to right is also n.
    """
    cars are moving right to left are left-aligned with the first car, so the first car will not collide with itself.
    return: number of collisions 
    """
    # Testing the function
    n = int(input("Enter the number of cars: "))
    collisions = car_race_collision(n)
    print(f"There are {collisions} collisions.")
    return collisions
```
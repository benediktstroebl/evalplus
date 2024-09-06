```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    Two cars are the important collision.
    However, the cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return:
    The function outputs the number of the collisions.
```

# Driver code
# Input number for cars
n = int(input("Enter the number of cars: "))

# Function call
result = car_race_collision(n)

print(result)
```
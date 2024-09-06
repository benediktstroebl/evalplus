```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars that are moving towards each other collide and they keep moving as if they did not collide. The function outputs the number of collisions.

n = int(input("Enter the number of cars: "))
collisions = 0
for i in range(n):
    car1 = i + 1
    car2 = n - i - 1
    if car1 > car2:
        if abs(car1 - car2) <= 1:
            collisions += 1
return collisions
```
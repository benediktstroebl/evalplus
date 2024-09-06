```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    All cars move in the same speed, with a small random factor, so they won't be identical. Two cars will
    scenario: one car is moving left to right and hits a car moving right to left. 
    The function outputs whether of a collision, based on the scenario above.
    """
    return n * ((n+1)/2)**2 - 1

#Test the function
n = int(input("Enter the number of cars: "))
print(car_race_collision(n))
```
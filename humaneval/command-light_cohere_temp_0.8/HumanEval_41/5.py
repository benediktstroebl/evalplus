Here is a self-contained Python script that defines a function car_race_collision, which simulates the described car race scenario:
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars
    are driving right to left. All cars have the specific speed and are infinitely sturdy, 
    as a result, they continue moving in their trajectory as if they did not collide.
    When function outputs the both the number of collisions and cars that cross each other.
    """
    set(range(n))
    cars = [list(map(lambda x: [x,x+1], set(range(n)))) for _ in range(n)]
    collisions = [list(zip(cars[i], cars[(i+1)%n])) for i in range(n)]
    return len(collisions), collisions
```
The function car_race_collision takes an integer n as input, which represents the number of cars on the road. The function creates a set of n range objects, each representing a potential car position. Then, it creates a list of n lists, each containing two elements: the current car and the next car. This process is map creates a pair of adjacent car positions for each set in the range object. Finally, the function creates a list of n pairs of cars by unzipping the corresponding lists from each set of cars. This process simulates the numbers of collisions between each pair of cars, and returns the number of collisions and a list of car pairs that cross each other.
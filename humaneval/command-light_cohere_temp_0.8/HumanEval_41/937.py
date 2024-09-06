```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    All cars have in same speed. Two cars will moving in the same speed collide and the collision time is 0.
    A car that's moving left to right hits a car that's moving right to left, but the cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    The function outputs the number of collisions.

return count = sum(map(lambda x:x!=0,range(n))))
``` 

This script defines a function `car_race_collision` that simulates the collision of cars on a straight road. It works by considering two sets of n cars, each moving in opposite directions along the road. The function outputs the count of collisions, which is the sum of the products of all elements in the `range(n)` set. 
This solution efficiently calculates the number of collisions using a `map` function to create the product of each element and then uses the `sum` function to get the total sum.
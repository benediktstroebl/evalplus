```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 

    two sets of cars start out being very far from each other. All cars move in the same speed and move infinitely sturdy. 
    Two cars will collide when a car that's moving left to right hits a car that's moving right to left. The cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.

    return: 
    return n

#Test the function
n = int(input())
result = car_race_collision(n)
print(result)
```
```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left. 
    Two sets of cars start out being very far from
    each other. All cars move in the same speed.
    Two cars are collide
    once the cars are infinitely sturdy and strong, 
    as a result, they continue moving in their trajectory as if they did not collide.
    Returns the number of collisions.
    """
 Cars should collide starting from the beginning of the road and 
    ending at the end.
    """
    This could number of cars that are driving left to right that 
    are going to collide with the first set of cars. 

n = 10 # We define the number of cars driving left to right

# The number of collisions is equal to the number of cars that are driving left to right, divided by 2. 
collisions = n // 2 

# The cars driving left to right are not equal, so we need to sort them first
# The first car is 0, the second is 1, etc.
# Let's call the first car the index 'i'
# The second is i + 1
# The last is n - 1
# We sort them in ascending order
# i < i + 1 < n - 1
# We can use this to create a list of indices
# and then use these to slice the list of cars driving right to left
# and create a new list of lengths
# i < n - 1
# collides = [i, i + 1] * [n - i - 1]
# We can now create a list of the indices of the collisions
# and pass this to a list comprehension to create the output
collides = list(range(n // 2))
collides = [collide[0] for collide in collides for i, j in zip(range(n), (i, i + 1, n - i - 1))]
return sum(collides)

# Test the function
print(car_race_collision(10))
```
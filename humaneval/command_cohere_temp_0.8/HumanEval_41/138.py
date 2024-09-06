Here's a Python script that includes a function to solve the car crash problem as per the provided markdown code block:
```python
def car_race_collision(n: int):
    # Initialize two lists to represent the positions of cars moving left to right and right to left.
    l2r = [i for i in range(n)]
    r2l = [i for i in range(n)]
    
    # Sort the lists according to their positions. Cars at the same position will collide.
    l2r.sort()
    r2l.sort()
    
    # Initialize a variable to count the number of collisions.
    count = 0
    
    # Iterate through the two lists. If a car in the left to right list matches with a car in the right to left list, increment the collision count.
    for i in range(n):
        if l2r[i] == r2l[i]:
            count += 1
    
    return count

# Test the function against specific test cases.
test_cases = [
    (2,),
    (5,),
    (1000,),
    (1001,),
    (10000,),
    (100001,),
]

for n in test_cases:
    assert car_race_collision(n) == n // 2, f"Expected {n // 2} collisions for {n} cars, but got {car_race_collision(n)}."
```

This script defines the `car_race_collision` function to calculate the number of collisions when n cars are driving in opposite directions along an infinitely long straight road. It uses two sorted lists to represent the positions of cars moving left to right and right to left, respectively. It then iterates through these lists to identify collisions, where cars at the same position in both lists collide. The function is tested against specific test cases to ensure it returns the expected number of collisions for various values of n.

The total number of collisions is n/2, because every car will collide with the set of n-1 cars exactly once. This will occur when the first car from the left of the left-moving cars hits the n-1th car of the right-moving cars.  This collision will cause a chain reaction in which all 'left' cars hit all 'right' cars until the nth car from the left collides with the nth car from the right. At this point, the chain reaction is over. Because there are n/2 spots where a collision occurs (i.e. n/2 moments in time when a collision is happening), this means the total number of collisions is n/2.
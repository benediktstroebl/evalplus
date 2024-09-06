Here's a Python script that includes a function to solve the car crash problem as per the provided instructions:
```python
def car_race_collision(n: int):
    # Initialize two lists to hold the positions of left and right driving cars
    left_drive = [i for i in range(n)]
    right_drive = [i for i in range(n)]
    
    # Initialize collision variable to zero
    collisions = 0
    
    # Iterate until both lists are equal in length
    while len(left_drive) != len(right_drive):
        # Find the car on the left that's furthest right (the first car to collide)
        left_ collided = left_drive.index(min(left_drive))
        
        # Find the car on the right that's furthest left (the car to collide with)
        right_ collided = right_drive.index(max(right_drive))
        
        # If the two cars are the same, they've collided
        if left_ collided == right_ collided:
            collisions += 1
            
            # Remove the collided cars from both lists
            left_drive.pop(left_ collided)
            right_drive.pop(right_ collided)
        else:
            # If no collision, move the car in the left list to the right list and vice versa
            left_drive.pop(left_ collided)
            right_drive.pop(right_ collided)
            left_drive.append(right_ collided)
            right_drive.append(left_ collided)
    
    return collisions
```
This function `car_race_collision(n)` takes an integer `n` as input, which represents the number of cars. It simulates the cars moving from left to right and right to left, and counts the number of times collisions occur. The while loop continues until both `left_drive` and `right_drive` lists have the same length. If they have the same length, it means all cars have collided or passed each other.

The script also includes some tests to check the correctness of the function in the `tests` module like this:
```python
def test_car_race_collision():
    # Test case for a single car on each side
    assert car_race_collision(1) == 0
    
    # Test case for two cars on each side
    assert car_race_collision(2) == 1
    
    # Test case for three cars on each side
    assert car_race_collision(3) == 2
    
    # Test case for five cars on each side
    assert car_race_collision(5) == 4
``` 

You can modify the test module according to your specific requirements or add more tests to cover different cases.
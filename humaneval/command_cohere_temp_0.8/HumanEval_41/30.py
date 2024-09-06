Here's a Python script that includes a function to solve the car collision problem described in the markdown code block:
```python
def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n)]
    
    # Initialize the collisions counter
    collisions = 0
    
    # Iterate until a car from the left and right lists cross each other's position
    for i in range(n):
        # Find the car on the right moving list that's at the same position as the current left moving car
        right_car_idx = right_cars[i]
        
        while len(right_cars) > right_car_idx:
            if right_cars[right_car_idx] == left_cars[i]:
                collisions += 1
                break
            right_car_idx += 1
        
    return collisions
```
This script defines the `car_race_collision` function, which takes in an integer `n` that represents the number of cars. It creates two lists, `left_cars` and `right_cars`, containing `n` cars each, representing the left and right moving cars respectively. It then iterates through the cars and for each car from the `left_cars` list, it finds the corresponding car in the `right_cars` list that's at the same position. If a matching car is found, it means they've collided, and the `collisions` counter is incremented. The function returns the total number of collisions after iterating through all the cars.

To test this function, you can add tests like:
```python
# Test case for when there's no collision
test_cases = [(1,), (2,), (5,), 10, 20]
expected_results = [0, 0, 0, 0, 0]
for i in range(len(test_cases)):
    assert car_race_collision(test_cases[i]) == expected_results[i]
```
This tests the function for different cases, asserting that the output matches the expected number of collisions for each case. 
The test cases can be expanded to cover a broader range of input values and edge cases to ensure the accuracy of the function.
Here's a Python script that contains a function which solves the car collision problem as per the provided markdown code block:
```python
def car_race_collision(n: int):
    # Define the two lists to store car positions for each team
    l1, l2 = [], []
    
    # Define the car positions for each team at different time steps
    for i in range(n):
        l1.append(i)
        l2.append(n - i - 1)
    
    # Find the collisions in the first n cars
    collisions = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l1[i] > l2[j] and l1[i] < l2[j] + n:
                collisions += 1
                break
    return collisions
```

This code defines two lists (`l1` and `l2`) to represent the positions of cars moving from left to right (`l1`) and right to left (`l2`). It then iterates through each car's position and checks if there's a collision with the cars moving from the opposite direction. When a collision is detected, it increments the `collisions` counter and breaks out of the inner loop to move on to the next car. The function returns the total collisions encountered.

To test this function, you can run the following code using the Python interpreter:
```python
test_cases = [
    (1, 1),
    (2, 0),
    (3, 4),
    (5, 10),
    (10, 45),
    (100000, 50000)
]

for n, expected in test_cases:
    assert car_race_collision(n) == expected
```

This block of code tests the function with different values of `n` and compares the returned value with the expected result.
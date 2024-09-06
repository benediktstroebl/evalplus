Here's a Python script that contains a function which solves the specified problem:
```python
def car_race_collision(n: int):
    cars_left = n // 2
    cars_right = n - cars_left
    collisions = 0

    for i in range(cars_left):
        for j in range(cars_right):
            if i != j:
                collisions += 1
    return collisions

# Tests
assert car_race_collision(5) == 4  # 4 collisions when n = 10: 5 cars on the left, 5 on the right, and 4 collisions
assert car_race_collision(11) == 10  # 10 collisions when n = 22: 11 cars on the left, 11 on the right, and 10 collisions
```

This function calculates the number of collisions by calculating the number of cars on the left (`cars_left`) and right (`cars_right`) and then counting the number of pairs that do not overlap, giving the number of collisions. 

This approach results in an O(n^2) time complexity, where n is the number of cars. It is efficient enough for practical purposes for this problem.
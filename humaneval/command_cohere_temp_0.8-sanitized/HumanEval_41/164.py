def car_race_collision(n):
    cars_left = n // 2
    cars_right = n - cars_left
    return max(0, cars_left + cars_right - 1)
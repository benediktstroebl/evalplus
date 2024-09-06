def car_race_collision(n: int):
    # Define 2 lists to store the positions of left and right driving cars.
    l_drivers = []
    r_drivers = []
    
    # Calculate the number of collisions when 'n' is odd.
    if n % 2 == 1:
        for i in range(n):
            l_drivers.append(i)
            r_drivers.append(n - 1 - i)

        collisions = 0
        for i in range(0, n, 2):
            if l_drivers[i] == r_drivers[i]:
                collisions += 1
            l_drivers[i] += 1
            r_drivers[i] -= 1

        return collisions
    
    # Calculate the number of collisions when 'n' is even.
    else:
        for i in range(n // 2):
            l_drivers.append(i)
            r_drivers.append(n - 1 - i)
        for i in range(n // 2):
            l_drivers.append(n - i - 1);
            r_drivers.append(i)

        collisions = 0
        for i in range(0, n, 2):
            if l_drivers[i] == r_drivers[i]:
                collisions += 1
            l_drivers[i] += 1
            r_drivers[i] -= 1

        return collisions
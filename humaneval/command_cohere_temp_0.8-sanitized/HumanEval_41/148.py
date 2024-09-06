def car_race_collision(n: int):
    # Define two lists to store car positions for each team
    team1 = [i for i in range(n)]
    team2 = [i for i in range(n, 2 * n)]

    # Initialize collisions as 0
    collisions = 0

    # Loop through all possible pairs of cars
    for i in range(n):
        for j in range(n):
            if i < n:
                if team1[i] + i <= team2[j]:
                    collisions += 1
            else:
                if team1[i] - (2 * n - i) <= team2[j]:
                    collisions += 1

    return collisions
def tri(n):
    progression = [0, 0, 0]
    for i in range(1, n + 1):
        if i % 2 == 0:
            progression.append(1 + i // 2)
        else:
            progression.append(progression[i - 1] + progression[i - 2] + progression[i + 1])
    return progression
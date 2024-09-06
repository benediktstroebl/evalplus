def f(n):
    facts = [0] * n
    for i in range(1, n+1):
        facts[i] = facts[i - 1] * i if i % 2 == 0 else facts[i - 1] + i
    return facts
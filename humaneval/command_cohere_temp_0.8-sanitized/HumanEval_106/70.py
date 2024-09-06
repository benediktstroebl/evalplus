def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i & -i - 1] = facts[i & -i - 1] * (i)
        sums[i] = sums[i - 1] + i
    return facts + sums
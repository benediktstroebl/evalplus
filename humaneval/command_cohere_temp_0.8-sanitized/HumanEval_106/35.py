def f(n):
    facts = [0] * n
    sums = [0] * n
    for i in range(1, n+1):
        facts[i & -i] = i
        if i % 2 == 0:
            continue
        for j in range(1, i+1):
            sums[i] += j
    return facts + sums
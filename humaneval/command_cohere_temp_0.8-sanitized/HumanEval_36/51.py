def fizz_buzz(n):
    counts = [0, 0, 0]
    for i in range(1, n+1):
        num = str(i)
        if len(num) == len(set(num)): # prime
            if i % 11 == 0 or i % 13 == 0:
                counts[num.count('7')] += 1
    return max(counts)
def tri(n):
    sequence, cache = [], [3, 1]
    for i in range(1, n+1):
      if i % 2 == 0:
        sequence.append(1 + i // 2)
        cache.append(sequence[-1])
      else:
        sequence.append(cache[i-1] + cache[i-2] + cache[i+1])
        cache.append(sequence[-1])
    return sequence
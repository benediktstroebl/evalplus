def tri(n):
    sequence, cache = [[1, 3], [3, 2, 8]], {}
    for i in range(1, n+1):
      if i % 2 == 0:
        sequence.append(int(sequence[-1][-1] + n / 2))
      else:
        sequence.append(int(sequence[i-2][-1] + sequence[i-1][-1] + sequence[i+1][-1]))
    for i in range(len(sequence)):
      cache[i] = sequence[i]
    return cache[0:]
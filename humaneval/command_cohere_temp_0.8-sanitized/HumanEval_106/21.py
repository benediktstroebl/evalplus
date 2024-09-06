def f(n):
    ls = [0] * n
    for i in range(1, n+1):
      j = i
      if i % 2 == 0:
        ls[i] = j
        while j > 1:
          j = j * (j - 1)
      else:
        ls[i] = sum(range(1, i+1))
    return ls
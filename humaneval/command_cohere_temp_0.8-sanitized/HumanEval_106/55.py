def f(n):
    ls = [0] * n
    for i in range(1, n+1):
      j = i // 2 + 1
      if i % 2 == 0:
        ls[i-1] = factorial(j)
      else:
        ls[i-1] = sum(range(1, j+1))
    return ls
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
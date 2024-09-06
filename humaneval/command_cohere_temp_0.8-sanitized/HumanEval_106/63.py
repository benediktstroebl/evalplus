def f(n):
    ans = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ans.append(factorial(i))
        else:
            ans.append(sum(range(1, i+1)))
    return ans
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
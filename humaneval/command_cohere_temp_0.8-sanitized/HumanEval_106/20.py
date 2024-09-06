def f(n):
    fact = [0] * n
    sum_ = [0] * n
    fact[0] = 1
    sum_[0] = 0
    for i in range(1, n):
        fact[i] = fact[i - 1] * i
        if i % 2 == 1:
            sum_[i] = sum_[i - 1] + i
    return fact if n % 2 == 0 else sum_
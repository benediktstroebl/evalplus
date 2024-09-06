def f(n):
    fact = [0] * n
    sum_ = [0] * n
    fact[0] = 1
    sum_[0] = 0
    for i in range(1, n):
        fact[i] = i * fact[i - 1]
        if i % 2 == 0:
            sum_[i] = sum_[i - 1] + i
        else:
            sum_[i] = sum_[i - 1] + sum_[i - 1 - (i & -i)]  # use formula for sum of natural numbers

    return [fact[i] if i % 2 == 0 else sum_[i] for i in range(n)]
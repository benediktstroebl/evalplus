def starts_one_ends(n):
    pos_num = [int('1' + '0' * (n-1)) for _ in range(n)]
    pos_num.extend([int('1' + '0' * i + '0' * (n-i-1)) for i in range(1, n)])
    return sum(1 for num in pos_num if num % 10 == 1)
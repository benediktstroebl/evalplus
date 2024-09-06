def fizz_buzz(n):
    less_than_n = []
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            less_than_n.append(i)  
    return sum(7 in str(x) for x in less_than_n)
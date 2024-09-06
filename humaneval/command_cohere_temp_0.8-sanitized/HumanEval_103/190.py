def rounded_avg(n, m):
    bin_str = [-1 if x > y else str(bin(x+y-1))[2:] for x, y in zip(range(n, m+1), range(n, m+1)+[n])]
    return '0b' + bin_str.pop() if bin_str.count(-1) % 2 else '0b' + '1' + bin_str.pop()
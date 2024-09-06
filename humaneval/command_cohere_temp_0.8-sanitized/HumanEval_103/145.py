def rounded_avg(n, m):
    bin_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return bin_str if bin_str[0] != '-' else '0b' + bin_str
n = int(input("Enter n: "))
m = int(input("Enter m: "))
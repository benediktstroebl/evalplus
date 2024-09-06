Here's the solution to the problem:

def fizz_buzz(n):
    m = 10
    count = 0
    for i in range(2, n+1):
        num = 0
        while m % 11 == 0 or m % 13 == 0 and num < n:
            m *= 10
        num += 1
        count += num >= n
    return count
def fizz_buzz(n):
    # Calculate the sum of digits in the range [1, n) that are divisible by 11 or 13 and subtract 1
    return sum(int(d) for d in range(1, n + 1) if d % 11 == 0 or d % 13 == 0) - 1
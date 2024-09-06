def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # consequent number is fibonacci number, alternates between adding and subtracting
        # previous number
        num1, num2 = 0, 1
        for _ in range(n - 2):
            num1, num2 = num2, num1 + num2
        return num2
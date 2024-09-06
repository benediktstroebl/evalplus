def f(n):
    # initialize a list of size n
    result = [0] * n
    # assign values to the list based on the given criteria
    for i in range(1, n+1):
        if i % 2 == 0:
            result[i-1] = factorial(i)
        else:
            result[i-1] = sum(range(1, i+1))
    return result
def factorial(n):
    # define a recursive function to calculate factorial
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
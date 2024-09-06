def f(n):
    # initialize a list of size n
    ret = [0] * n
    # iterate through the indices from 1 to n
    for i in range(1, n+1):
        # if the index is even, set the list element to the factorial of i
        if i % 2 == 0:
            ret[i-1] = factorial(i)
        # if the index is odd, set the list element to the sum of numbers from 1 to i
        else:
            ret[i-1] = sum(range(1, i+1))
    # return the list
    return ret
def factorial(n):
    # initialize the result to 1
    result = 1
    # iterate through the numbers from 2 to n
    for i in range(2, n+1):
        # multiply the result by i
        result *= i
    # return the result
    return result
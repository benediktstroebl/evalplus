def f(n):
    # Initialize an empty list to hold the results
    result = []
    
    # Iterate through 1 to n inclusive
    for i in range(1, n + 1):
        # If the index i is even, calculate the factorial of i
        if i % 2 == 0:
            result.append(factorial(i))
        # If the index i is odd, calculate the sum of numbers from 1 to i
        else:
            result.append(sum(range(1, i + 1)))
    
    # Return the list of calculated values
    return result
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
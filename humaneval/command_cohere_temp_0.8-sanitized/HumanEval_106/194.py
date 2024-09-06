def f(n):
    # Initialize an empty list to store the final results
    result = []
    
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the current number 'i' is even, calculate the factorial of 'i'
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number 'i' is odd, calculate the sum of numbers from 1 to 'i'
        else:
            result.append(sum(range(1, i+1)))
    
    # Finally, return the computed list of results
    return result
def factorial(n):
    # Implement factorial function using recursion
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
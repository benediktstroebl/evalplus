def f(n):
    # Initialize an empty list to hold the results
    result = []
    
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n + 1):
        # If the current number 'i' is even, calculate its factorial
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number 'i' is odd, calculate its sum from 1 to i
        else:
            result.append(sum(range(1, i + 1)))
    
    # Return the list of computed values
    return result
def factorial(n):
    # Implement factorial function for n
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def f(n):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the values from 1 to n
    for i in range(1, n + 1):
        # If the index 'i' is even, calculate the factorial of i
        if i % 2 == 0:
            result.append(factorial(i))
        # If the index 'i' is odd, calculate the sum of numbers from 1 to i
        else:
            result.append(sum(range(1, i + 1)))
    
    # Return the final list of results
    return result
def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # Iterate through the values from 2 to 'n'
    for i in range(2, n + 1):
        # Multiply the current number with the running result
        result *= i
    
    # Return the final factorial result
    return result
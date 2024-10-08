def f(n):
    # Initialize an empty list to store the final results
    result = []
    
    # Iterate through the values from 1 to n in increments of 2
    for i in range(1, n + 1, 2):
        # If the current value is even, calculate the factorial of i
        if i % 2 == 0:
            result.append(factorial(i))
        # Otherwise, calculate the sum of numbers from 1 to i and add it to the list
        else:
            result.append(sum(range(1, i + 1)))
    
    # Return the final list of results
    return result
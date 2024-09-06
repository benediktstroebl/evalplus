def f(n):
    # Initialize an empty list to store the results
    result = []
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the current number is even, calculate the factorial of that number
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current number is odd, calculate the sum of numbers from 1 to that number
        else:
            result.append(sum(range(1, i+1)))
    # Return the list of results
    return result
def factorial(n):
    # Initialize the result to 1
    result = 1
    # Iterate through the range of numbers from 1 to n
    for i in range(1, n+1):
        # Multiply the result by the current number
        result *= i
    # Return the factorial of n
    return result
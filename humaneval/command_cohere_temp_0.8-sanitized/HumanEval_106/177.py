def f(n):
    # Initialize an empty list to store the final result
    result = []

    # Iterate through the range of numbers from 1 to n
    for i in range(1, n + 1):
        # If the current index 'i' is even, calculate the factorial of 'i'
        if i % 2 == 0:
            result.append(factorial(i))
        # If the current index 'i' is odd, calculate the sum of numbers from 1 to 'i'
        else:
            result.append(sum(range(1, i + 1)))

    # Return the final list containing the computed results
    return result
def factorial(n):
    # Initialize the result to 1
    result = 1

    # Iterate through the range of numbers from 1 to 'n'
    for i in range(1, n + 1):
        # Multiply the current number 'i' with the accumulating result
        result *= i

    # Return the final factorial value
    return result
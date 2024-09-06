def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression that yields integers from 0 to n-1.
    x = (i for i in range(n))
    # Use a list comprehension to filter out numbers that are divisible by 11 or 13.
    numbers = [i for i in x if i%11==0 or i%13==0]
    # Use a sum function to calculate the total number of 7s in the list of numbers.
    return sum(int(j)/7 for j in numbers)
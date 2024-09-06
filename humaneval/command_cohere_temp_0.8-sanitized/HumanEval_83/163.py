def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting digits,
    # so the largest number considered is 99999...99 (10^n - 1) to account
    # for the possibility of starting with a 1.
    numbers = [0] * int(10 ** n)
    
    # Count numbers starting with 1
    numbers[1] = 1
    
    # Count numbers that end with 1
    for i in range(2, 10 ** n - 1):
        numbers[i] += 1
        numbers[10 ** n - i] += 1
    
    return sum(numbers)

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # create a list of the first 10 1-digit numbers, the first 100 2-digit
    # numbers, the first 1000 3-digit numbers, and so on until the first 10
    # n-digit numbers
    numbers = []
    for i in range(1, 11):
        numbers += list(range(10 ** (i - 1), 10 ** i))
    
    # count the number of numbers in numbers that start with 1, or end with 1
    count = 0
    for num in numbers:
        if num % 10 == 1 or num // 10 ** (len(str(num)) - 1) == 1:
            count += 1
    
    # return the result of dividing the count by n, since there are n-digit
    # numbers in the list
    return count // 10 ** (n - 1)

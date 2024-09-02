
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # TODO: Implement the solution using a single pass through the array.
    # The time complexity should be O(n).
    # The space complexity should be O(1).
    count = 0
    for num in range(n+1):
        if (num % 10 == 1):
            count += 1
    return count

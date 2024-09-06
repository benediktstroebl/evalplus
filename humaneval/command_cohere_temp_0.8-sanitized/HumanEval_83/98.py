def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting with 1 and
    # ending with 1, starting with 1 and ending with 11, and so on.
    counts = [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    return counts[-1] if n == 1 else sums(counts[:n]) - sums(counts[:n - 1])
def sums(numbers):
    # If there is only one number, return it. Otherwise, return the sum of
    # all the numbers in the list minus the sum of all the numbers in the
    # list minus 1 (to account for the counting double-counting the single
    # digits).
    if len(numbers) == 1:
        return numbers[0]
    return sum(numbers) - sum(x for x in numbers if x != numbers[0])
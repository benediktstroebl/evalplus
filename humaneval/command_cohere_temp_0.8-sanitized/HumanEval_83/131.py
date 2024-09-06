def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1.
    count = [0] * (n + 1)
    # Initialize the starting and ending numbers.
    start_one = 1
    end_one = 10 ** n
    # Loop through the numbers and increment the count for the numbers starting or ending with 1.
    for i in range(2, end_one):
        if i >= start_one and i <= end_one and i % 10 == 1:
            count[len(str(i))] += 1
        elif i == end_one:
            count[len(str(i))] -= 1
        elif i >= start_one:
            count[len(str(i))] -= 1
        i += 1
    # Return the total count of numbers starting or ending with 1.
    return sum(count)
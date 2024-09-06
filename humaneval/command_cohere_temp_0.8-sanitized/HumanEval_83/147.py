def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a possible list of n-digit numbers from 1 to n*10^n
    num_list = list(range(n*10**n, 0, -1))
    # Filter the list to include only numbers that start or end with 1.
    filtered_list = [i for i in num_list if (i//10 + i%10)%10 == 1 or i%10 == 1]
    return len(filtered_list)
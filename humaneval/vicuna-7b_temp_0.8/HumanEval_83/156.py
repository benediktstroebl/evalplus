
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Build the list of n-digit numbers
    nums = str(n) + '0'
    nums_list = nums.split()

    # Count the numbers of n-digit numbers that start with 1
    start_ones = [i for i in nums_list if i[0] == '1']
    start_ones_count = len(start_ones)

    # Count the numbers of n-digit numbers that end with 1
    end_ones = [i for i in nums_list if i[-1] == '1']
    end_ones_count = len(end_ones)

    # Return the sum of the start and end count
    return start_ones_count + end_ones_count

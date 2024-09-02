
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # #This function works and gives correct result, but it is too slow for the
    # #appropriate input size
    # #Returns a list of numbers that start with one
    # ones_start = [10**(n-1)]
    # #Returns a list of numbers that end with one
    # ones_end = [10**n]
    # for i in range(1, n):
    #     #Appends numbers to list of numbers that start with one
    #     ones_start.append(10**i * ones_start[i-1])
    #     #Appends numbers to list of numbers that end with one
    #     ones_end.append(10**i * ones_end[i-1])
    # #Sums list of numbers that start with one
    # total_start = sum(ones_start)
    # #Sums list of numbers that end with one
    # total_end = sum(ones_end)
    # #Returns the total count of the numbers that start or end with 1
    # return total_start + total_end - ones_end[0]
    
    # #This function works and gives correct result, but it is too slow for the
    # #appropriate input size
    # #Returns a list of numbers that start with one
    # ones_start = [10**(n-1)]
    # #Returns a list of numbers that end with one
    # ones_end = [10**n]
    # for i in range(1, n):
    #     #Appends numbers to list of numbers that start with one
    #     ones_start.append(10**i * ones_start[i-1])
    #     #Appends numbers to list of numbers that end with one
    #     ones_end.append(10**i * ones_end[i-1])
    # #Sums list of numbers that start with one
    # total_start = sum(ones_start)
    # #Sums list of numbers that end with one
    # total_end = sum(ones_end)
    # #Returns the total count of the numbers that start or end with 1

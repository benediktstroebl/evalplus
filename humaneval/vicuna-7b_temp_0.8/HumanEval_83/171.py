
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Build a list of all n-digit numbers
    digits = [str(d) for d in range(10)]
    n_list = [1]
    for i in range(n):
        n_list.append(n_list[i])
    # Check if n-digit numbers start or end with 1
    count = 0
    for i in range(len(n_list)):
        if n_list[i] == "1" or n_list[i].startswith("1"):
            count += 1
    return count

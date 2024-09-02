
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # edge cases
    if n < 3:
        return 0
    if n == 3:
        return 1

    # frequencies dictionary
    freq = {}
    # sum of the product of each number
    s = 0
    # solution
    sol = 0

    # iterate over the numbers
    for num in range(1, n + 1):
        # calculate the square of the number
        num_squared = num * num
        # calculate the sum
        s += num_squared - num + 1
        # add to the frequencies dictionary
        if s % 3 in freq:
            freq[s % 3] += 1
        else:
            freq[s % 3] = 1
    # iterate over the frequencies
    for key, value in freq.items():
        # if the frequency of the sum is more than 2
        if value > 2:
            # add to the solution
            sol += value * (value - 1) * (value - 2) // 6
        # else if the frequency of the sum is more than 1
        elif value > 1:
            # add to the solution
            sol += value * (value - 1) // 2
    # return the solution
    return sol


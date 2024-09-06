
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
    # initializing number of valid triples to 0
    num_triples = 0

    for i in range(1, n):
        # calculating the next valid number in the array
        next_valid_num = i * i - i + 1

        # checking if the next valid number is a multiple of 3
        if next_valid_num % 3 == 0:
            # incrementing the number of valid triples by 1
            num_triples += 1

    # returning the number of valid triples
    return num_triples

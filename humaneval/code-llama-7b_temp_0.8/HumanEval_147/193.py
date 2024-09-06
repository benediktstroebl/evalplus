
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

    # Create a list of values
    values = list(range(1, n + 1))

    # Get the product of values
    value_products = [a * b for a in values for b in values]

    # Filter the product that satisfy the condition
    valid_products = list(filter(lambda x: x % 3 == 0, value_products))

    # Get the valid products
    valid_triplets = [[values[index // len(values)]] * 3 for index in valid_products]

    # Flatten the list of list
    valid_triplets = [item for sublist in valid_triplets for item in sublist]

    # Get the frequency of valid triplets
    from collections import Counter
    valid_triplet_counts = Counter(valid_triplets)

    # Get the max valid triplets
    max_triples = max(valid_triplet_counts.values())

    return max_triples


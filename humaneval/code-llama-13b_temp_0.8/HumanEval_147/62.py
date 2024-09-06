
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
    # Array for our output numbers
    a = []

    # Loop over each index in the array.
    # We will be using the value of the index for the current item
    for i in range(n):

        # Set the current value at the index to the current index
        # squared minus the index.
        a.append(i ** 2 - i)

    # The number of triples variable
    num_triples = 0

    # Loop over each index in the array.
    for i in range(n - 1):

        # Set the current value to the value at the current index
        curr = a[i]

        # Set the left pointer to the index after the current index.
        left = i + 1

        # Set the right pointer to the last index.
        right = n - 1

        # Loop over the left and right pointer while the left pointer
        # is less than the right pointer
        while left < right:

            # Set the current sum to the current value, the value at the left
            # index, and the value at the right index.
            curr_sum = curr + a[left] + a[right]

            # If the current sum is a multiple of 3, add 1 to the number of triples.
            if curr_sum % 3 == 0:
                num_triples += 1

            # Increment the left pointer.
            left += 1

            # Decrement the right pointer.
            right -= 1

    # Return the number of triples
    return num_triples


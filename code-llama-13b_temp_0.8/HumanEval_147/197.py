
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
    
    # List of possible remainders
    rem = [0, 1, 2]
    
    # Create an empty dictionary
    freq_of_rem = dict()
    
    # For each remainder, set the value to 0 in the dictionary
    for r in rem:
        freq_of_rem[r] = 0
        
    # Initialize result
    ans = 0
    
    # For each integer from 1 to n
    for i in range(1, n + 1):
        # Get the remainder when (i * i - i + 1) is divided by 3
        rem_i = (i * i - i + 1) % 3
        
        # Increment the frequency of the remainder
        freq_of_rem[rem_i] += 1
        
    # For each remainder
    for i in range(1, 3):
        # For each other remainder
        for j in range(i + 1, 3):
            # If the frequency of the remainders is greater than zero
            if freq_of_rem[i] * freq_of_rem[j] > 0:
                # Find the value to be subtracted
                val = (i - j) % 3
                
                # If the value to be subtracted is zero
                if val == 0:
                    # Increment the result by the frequency of the remainders
                    ans += freq_of_rem[i] * freq_of_rem[j]
                    
                # Else if the value to be subtracted is not zero
                else:
                    # Decrement the result by the frequency of the remainders
                    ans -= freq_of_rem[i] * freq_of_rem[j]
                    
    return ans
    

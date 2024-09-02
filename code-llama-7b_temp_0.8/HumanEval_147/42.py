
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
    # Input: n = 5
    # Output: 1
    # Explanation: 
    # a = [1, 3, 7, 13, 21]
    # The only valid triple is (1, 7, 13).

    #pseudocode:
    #
    #create an array of length n, a
    #loop from 1 to n, for each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1
    #return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    #and a[i] + a[j] + a[k] is a multiple of 3.


    # return a list with the length of n.
    # each index of the list should be i * i - i + 1. 
    #the value of a[i] = i * i - i + 1.
    arr = []
    for i in range(n):
        arr.append((i * i - i + 1))

    print(arr)

    #loop through each index of arr
    #if the index is less than the next index, and the next index is less than the last index, then the values of the first two indices (a[i], a[j]) are valid triples.

    count = 0
    for i in range(len(arr) - 2):
        if(arr[i] < arr[i+1] and arr[i+1] < arr[i+2]):
            count += 1

    print(count)


    # for i in range(len(arr) - 2):
    #     if(arr[i] < arr[i+1] and arr[i+1] < arr[i+2]):
    #         count += 1

    # return count


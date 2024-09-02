
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
    # To count the number of integers which are multiples of 3, we keep count of 
    # the number of multiples of 3 in the array A, and the number of multiples of 
    # 3 in B, and subtract the latter from the former. We first calculate the 
    # number of multiples of 3 in the array A. 
    # 
    # Each element in the array is itself a multiple of 3, so the number of 
    # multiples of 3 is equal to the length of the array. So, there are n * n 
    # such integers in the array A. 
    # 
    # We next find out the number of integers which are multiples of 3 in the 
    # array B. The elements in the array are the squares of the integers in A. 
    # If we take the squares of every third integer, we get a third of the numbers. 
    # So, we can get a third of the number of multiples of 3 in A by dividing n * n 
    # by 3. 
    # 
    # Finally, we calculate the number of multiples of 3 in C. The elements in the 
    # array C are the cubes of the integers in A. If we take the cubes of every 
    # third integer, we get a third of the numbers. So, we can get a third of the 
    # number of multiples of 3 in A by dividing n * n by 3. 
    # 
    # If we subtract the number of multiples of 3 in B from the number of multiples 
    # of 3 in A, and then subtract the number of multiples of 3 in C from the 
    # result, we will get the number of integers which are multiples of 3 in A 
    # which are not in B or C. 
    # 
    # For example, let's say n = 5. Then the elements in A are 1, 2, 3, 4, and 5. 
    # The squares of every third element are 1, 4, and 9. So, there are three 
    # multiples of 3 in B. 

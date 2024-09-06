
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    #########################
    # IMPORTS
    #########################

    from collections import Counter

    #########################
    # BOILERPLATE CODE
    #########################

    # # print(arr)
    # # print(k)

    # # HERE WE HAVE TO SOLVE THE PROBLEM

    # # print(result)

    # # return result
    return sum([arr[i] for i in range(k) if len(str(arr[i])) < 3])

    # # ALTERNATIVE SOLUTION
    # # we can use counter

    # c = Counter(arr[:k])
    # total = 0
    # for i in c.keys():
    #     if len(str(i)) < 3:
    #         total += i * c[i]

    # return total


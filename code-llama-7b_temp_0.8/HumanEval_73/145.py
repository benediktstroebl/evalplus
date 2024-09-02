
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Solution 1: Brute force
    # O(N^2)
    #     palindromes = []
    #     for i in range(0, len(arr)):
    #         for j in range(i, len(arr)):
    #             if len(arr[i:j+1]) > 1:
    #                 palindromes.append(arr[i:j+1])
    #     palindromes = list(set(palindromes))
    #     print(palindromes)
    #     return min(palindromes, key=len)
    #
    # Solution 2: Fastest
    # O(N)
    forwards = []
    backwards = []
    for i in range(len(arr)):
        forwards.append(arr[i:])
        if i != len(arr) - 1:
            backwards.append(arr[:i + 1][::-1])

    forwards = list(map(tuple, forwards))
    backwards = list(map(tuple, backwards))
    palindromes = forwards + backwards
    palindromes = list(set(palindromes))
    palindromes.sort(key=len)
    return palindromes[0]


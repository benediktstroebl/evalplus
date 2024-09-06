
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
    n = len(arr)
    min_change = float('inf')
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited:
                min_change = min(min_change, (j-i+1)//2 + 1)
                visited.add((i,j))
    return min_change

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

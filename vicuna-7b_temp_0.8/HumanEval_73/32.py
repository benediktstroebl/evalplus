
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
    def dfs(arr, start, end, path):
        """
        DFS helper function to find the minimum number of elements that need to be changed
        to make the array palindromic.

        :param arr: the input array
        :param start: the starting index of the range to check
        :param end: the ending index of the range to check
        :param path: a list that will be appended to with the path of the elements that have been
                     visited in the DFS
        :return: the minimum number of elements that need to be changed to make the array
                 palindromic
        """
        if (start <= end) and (arr[start] == arr[end]) and (start not in path):
            path.append(start)
            dfs(arr, end + 1, len(arr), path)
            path.pop()
            dfs(arr, start - 1, end, path)
            path.pop()
        return path[-1]

    path = [None] * len(arr)
    path[0] = 0
    path[1] = 1
    dfs(arr, 0, len(arr) - 1, path)
    return path[-1]

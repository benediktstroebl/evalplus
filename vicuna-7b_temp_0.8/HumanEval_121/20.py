
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    def dfs(lst, i):
        if i == len(lst):
            return lst[i] if lst[i] > 0 else -1
        if lst[i] > 0:
            return dfs(lst, i+1) + lst[i]
        return dfs(lst, i+1) - lst[i]

    s = 0
    for num in lst:
        if num % 2 != 0:
            s += dfs(lst, num // 2)
    return s


def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    def dfs(lst, cur=0, memo=None):
        if not memo:
            memo = {}
            memo[cur] = dfs(lst, cur+1, memo) if cur < len(lst) else 0
        if cur in memo:
            return memo[cur]
        memo[cur] = lst[cur]
        for i in range(1, len(lst)):
            if lst[cur] == lst[i]:
                cur = i
                dfs(lst, cur+1, memo)
        return memo[cur]
    result = dfs(lst)
    return result


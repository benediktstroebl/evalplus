
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    dp = [0] * (max(lst) + 1)
    dp[0] = 1
    for i in range(1, max(lst) + 1):
        if lst[i] == i:
            dp[i] = dp[i-1] + 1
        else:
            for j in range(i+1, max(lst) + 1):
                if lst[j] > lst[i]:
                    dp[i] = max(dp[i], dp[j-1] + 1)
    return dp[-1]

lst = [1,2,2,3,1]
result = search(lst)

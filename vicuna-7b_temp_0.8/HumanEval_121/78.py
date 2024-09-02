
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 在列表中查找所有標準寫法的倍數
    n = len(lst)
    for i in range(n // 2):
        j = i + 1
        while j < n:
            if lst[i] % 2 != lst[j] % 2:
                break
            j += 1
    odd_sum = 0
    for i in range(n):
        if lst[i] % 2 == 1:
            odd_sum += lst[i]
    return odd_sum

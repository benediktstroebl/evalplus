
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
    # Write your code here

    # best solution
    # lst.sort()
    # for i in range(len(lst)):
    #     if lst[i] == 0:
    #         continue
    #     if lst[i] >= i+1 and lst.count(lst[i]) >= lst[i]:
    #         return lst[i]
    # return -1

    # 56 ms
    # best solution
    # sorted_lst = sorted(lst)
    # for i in range(len(sorted_lst)):
    #     if sorted_lst[i] == 0:
    #         continue
    #     if sorted_lst[i] >= i+1 and lst.count(sorted_lst[i]) >= sorted_lst[i]:
    #         return sorted_lst[i]
    # return -1

    # 78ms
    # lst.sort()
    # i = 0
    # while i < len(lst):
    #     if lst[i] == 0:

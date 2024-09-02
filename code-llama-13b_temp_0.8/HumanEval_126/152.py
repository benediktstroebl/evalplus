
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # lst1=[]
    # lst2=[]
    # for i in range(len(lst)):
    #     if lst[i] not in lst1:
    #         lst1.append(lst[i])
    # for i in range(len(lst)):
    #     if lst[i] not in lst2:
    #         lst2.append(lst[i])
    # if lst1==lst2:
    #     return True
    # else:
    #     return False
    
    # lst1=[]
    # lst2=[]
    # for i in range(len(lst)):
    #     if lst[i] not in lst1:
    #         lst1.append(lst[i])
    # for i in range(len(lst)-1):
    #     if lst[i] > lst[i+1]:
    #         lst2.append(lst[i])
    # if lst1==lst2:
    #     return True
    # else:
    #     return False
    
    # for i in range(len(lst)-1):
    #     if lst[i] > lst[i+1]:
    #         return False
    # return True
    
    # lst1=[]
    # for i in range(len(lst)-1):
    #     if lst[i] > lst[i+1]:
    #         return False
    #     if lst[i] not in lst1:
    #         lst1.append(lst[i])
    # return lst1==lst
    
    # lst1=[]
    # for i in range(len(lst)):
    #     if lst[i] not in lst1:
    #         lst1.append(lst[i])
    # for i in range(len(lst)-1):
    #     if lst[i] > lst[i+1]:
    #         return False
    # return lst1==lst

    # lst1=[]
    # for i in range(len(lst)):
    #     if lst[i] not in lst1:
    #         lst1.append(lst[i])
    # for i in range

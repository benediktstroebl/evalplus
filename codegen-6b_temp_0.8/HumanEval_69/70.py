
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
    
    lst.sort(reverse=True)
    
    count = {}
    
    for i in lst:
        
        if count.get(i,0) == 0:
            return i
        else:
            count[i] = count[i] + 1
    
    return -1

test_lst1 = [4, 1, 2, 2, 3, 1]
test_lst1_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst1_3 = [5, 5, 4, 4, 4]

test_lst2 = [4, 1, 2, 2, 3, 1]
test_lst2_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst2_3 = [5, 5, 4, 4, 4]

test_lst3 = [4, 1, 2, 2, 3, 1]
test_lst3_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst3_3 = [5, 5, 4, 4, 4]

test_lst4 = [4, 1, 2, 2, 3, 1]
test_lst4_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst4_3 = [5, 5, 4, 4, 4]

test_lst5 = [4, 1, 2, 2, 3, 1]
test_lst5_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst5_3 = [5, 5, 4, 4, 4]

test_lst6 = [4, 1, 2, 2, 3, 1]
test_lst6_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
test_lst6_3 = [5, 5, 4, 4, 4]

test_lst7 = [4, 1, 2, 2, 3, 1]
test_l
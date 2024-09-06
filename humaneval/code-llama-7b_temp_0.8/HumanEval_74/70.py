
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # Create a function total_match with the following paramters: lst1, lst2
    # Create a variable total1 and set it to the sum of the strings in lst1
    # Create a variable total2 and set it to the sum of the strings in lst2
    # Create a variable total_lst1 and set it to the length of lst1
    # Create a variable total_lst2 and set it to the length of lst2
    # Create a variable count_lst1 and set it to the length of the list lst1
    # Create a variable count_lst2 and set it to the length of the list lst2
    # Create a variable min_count and set it to the minimum of total_lst1 and total_lst2
    # Create a variable new_lst1 and set it to the list []
    # Create a variable new_lst2 and set it to the list []
    
    def total_match(lst1, lst2):
        total1 = 0
        for i in range(0, len(lst1)):
            total1 += len(lst1[i])
        
        total2 = 0
        for i in range(0, len(lst2)):
            total2 += len(lst2[i])
        
        total_lst1 = len(lst1)
        total_lst2 = len(lst2)
        count_lst1 = 0
        count_lst2 = 0
        for i in range(0, len(lst1)):
            if total1 < total2:
                count_lst1 += 1
        for i in range(0, len(lst2)):
            if total2 < total1:
                count_lst2 += 1
        min_count = min(count_lst1, count_lst2)
        new_lst1 = []
        new_lst2 = []
        for i in range(0, min_count):
            new_lst1.append(lst1[i])
            new_lst2.append(lst2[i])
        if total1 == total2:
            return lst1
        elif total1 < total2:
            return new_lst1
        elif total1 > total2:
            return new_lst2
    

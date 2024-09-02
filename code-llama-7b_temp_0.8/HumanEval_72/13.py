
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''

    #create empty list to store the numbers
    lst = []
    
    #loop to add numbers to list
    for x in range(q):
        lst.append(int(input()))
        
    #print(lst)

    #create empty list to store the numbers
    lst2 = []
    
    #loop to add numbers to list
    for x in range(w):
        lst2.append(int(input()))
        
    #print(lst2)
    
    #loop through the numbers in list and add them
    total = 0
    for i in lst:
        total += i

    #print(total)

    #loop through the numbers in list and add them
    total2 = 0
    for i in lst2:
        total2 += i

    #print(total2)
    
    #check if total is less than or equal to total 2
    if total <= total2:
        #loop through list to see if it is a palindrome
        for i in range(len(lst)):
            if lst[i] != lst[len(lst)-i-1]:
                return False
            else:
                return True
    
    else:
        return False




def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    #l_new = []
    #for item in l:
        #if item%3 == 0:
            #l_new.append(item)
        #else:
            #l_new.append(item)
            
    #l_new.sort()
    #return l_new
    #len_l = len(l)
    #l_index = 0
    #for index in range(0, len_l-1):
        #if index%3 == 0:
            #l_index += 1
        #else:
            #l[index], l[l_index] = l[l_index], l[index]
            #l_index += 1
            
    #return l
    #for index in range(0, len_l-1):
        #if index%3 == 0:
            #l_index += 1
            #for index_2 in range(0, len_l-1):
                #if index_2%3 == 0:
                    #l_index += 1
                #else:
                    #l[index_2], l[l_index] = l[l_index], l[index_2]
                    #l_index += 1
   
    ##another way
    #for index in range(0, len_l-1):
        #if index%3 == 0:
            #l_index += 1
            #for index_2 in range(index, len_l-1):
                #if index_2%3 == 0:
                    #l_index += 1
                #else:
                    #l[index_2], l[l_index] = l[l_index], l[index_2]
                    #l_index += 1
                    
    #l[index], l[l_index] = l[l_index], l[index]
    #return l
    
    #Another way
    for index_1 in range(0,len(l)-1):
        for index_2 in range(index_1+1, len(l)):
            if index_2%3 ==0:
                if index_2 == index_1:
                    continue
            if index_1%3 == 0:

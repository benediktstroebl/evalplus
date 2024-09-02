
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    #sort the list
    lst = sorted(lst)
    #check if the list is not empty
    if len(lst) > 0:
        #initialize variables to check if even numbers are present in the list
        even_found = False
        even = 0
        #loop through the elements of the list
        for i in range(len(lst)):
            #check if the element is even or odd
            if lst[i] % 2 == 0:
                #if even, increment even and update the index
                even = lst[i]
                i += 1
                even_found = True
            else:
                #if odd, increment the index
                i += 1
        #if even number is present in the list
        if even_found:
            #return the even number
            return even
        else:
            #return an empty list
            return []
    else:
        #return an empty list
        return []

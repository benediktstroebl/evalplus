
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    def index_of_second_smallest(lst):
        """
        Returns the index of the 2nd smallest item of a list.
        Returns -1 if the list contains less than 2 items.
        """
        min1 = min2 = 9999999
        for i, num in enumerate(lst):
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2 and num!= min1:
                min2 = num
        if min2 == 9999999:
            return -1
        else:
            return lst.index(min2)
    
    index = index_of_second_smallest(lst)
    if index >= 0:
        return lst[index]
    else:
        return None

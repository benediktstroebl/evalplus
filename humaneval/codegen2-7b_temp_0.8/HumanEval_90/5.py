
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
    def find_next_smallest(lst):
        def find_next_smallest_helper(lst, index):
            if index == len(lst) - 1:
                return None
            else:
                if lst[index + 1] < lst[index]:
                    return lst[index + 1]
                else:
                    return find_next_smallest_helper(lst, index + 1)
        return find_next_smallest_helper(lst, 0)
    return find_next_small

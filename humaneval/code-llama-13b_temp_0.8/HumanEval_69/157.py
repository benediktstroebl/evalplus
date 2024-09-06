
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
    # your code here
    # The most straightforward way is to just iterate through the list of integers and count the frequencies, 
    # but that would have a time complexity of O(n2), which is very inefficient.
    # We can do better by first sorting the list, which would have a time complexity of O(nlogn), then finding the solution in linear time.
    # We sort the list and iterate through it, keeping track of the current frequency count and the current answer.
    # As we iterate through the list, we keep track of the current frequency count and the current answer.
    # If the current element is greater than or equal to the current frequency count, 
    # then we replace the answer with the current element, 
    # and increase the current frequency count by 1.
    # If the current element is less than the current frequency count, 
    # then we check if the current element is less than or equal to the answer. 
    # If it is, then we replace the answer with the current element.
    # If the current element is less than the answer, 
    # then we only replace the answer if the current frequency count is greater than or equal to 2.
    # We can't replace the answer with the current element if the current frequency count is less than 2, 
    # because we need a frequency greater than or equal to the value of the integer itself.
    
    lst.sort()
    answer = -1
    current_frequency = 0
    
    for i in lst:
        if i == 0:
            continue
        
        if i >= current_frequency:
            current_frequency += 1
            answer = i
            
        elif i < answer:
            if current_frequency >= 2:
                answer = i
            
    return answer

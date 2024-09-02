
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
    # Use a counter to keep track of the frequency of each number
    freq = {}
    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    # Use a queue to keep track of the numbers that haven't been processed yet
    queue = []

    while freq:
        # Get the next number to process from the list
        num = min(freq.keys(), key=freq.get)

        # If the number has the desired frequency, return it
        if freq[num] >= num:
            return num

        # Remove the number from the list
        freq.pop(num)

        # Add the number to the queue
        queue.append(num)

    # If all numbers have been processed and no number was found with the desired frequency, return -1
    return -1

lst = [1, 2, 2, 3, 1]

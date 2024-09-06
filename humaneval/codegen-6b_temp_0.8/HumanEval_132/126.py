
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # create queue
    queue = []
    # create a set that keeps track of what is in queue
    queue_set = set()
    # iterate through the string
    for bracket in string:
        # if the bracket is not a closing bracket
        # then add it to the queue
        if bracket != ']' and bracket != '}':
            queue.append(bracket)
            queue_set.add(bracket)
        # if the bracket is not a opening bracket
        # then pop the queue to see if the queue is empty
        # and if it is not empty, then check to see if the closing bracket is nested
        # if the closing bracket is not nested, there is no valid subsequence
        # so return False
        elif bracket != '(' and bracket != '[' and bracket != '{':
            if queue:
                first = queue.pop()
                if first != bracket:
                    return False
            else:
                return False
    # if there are still brackets in the queue, then there is a nested sequence
    return queue


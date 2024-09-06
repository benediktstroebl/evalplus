
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
    # use a queue to keep track of the brackets we have seen
    # if we see an opening bracket, check that it's followed by a closing bracket and add it to the queue
    # if we see a closing bracket, check that it's followed by an opening bracket and if so, delete the element at the front of the queue
    queue = []
    for char in string:
        if char == '[':
            queue.append(char)
        elif char == ']':
            # the element at the front of the queue is the closing bracket
            if len(queue) == 0:
                return False
            elif queue[0] == '[':
                queue.pop(0)
            else:
                return False
    return True

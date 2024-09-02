
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

    
    def find_matching_brackets(list_of_brackets):
        open_brackets = []
        for index, bracket in enumerate(list_of_brackets):
            if bracket == '[':
                open_brackets.append(index)
            elif bracket == ']':
                if len(open_brackets) == 0:
                    return -1
                else:
                    return open_brackets.pop()
        if len(open_brackets) == 0:
            return len(list_of_brackets)
        else:
            return -1
    
    i = 0
    while i < len(string):
        if string[i] == '[' or string[i] == ']':
            subseq_brackets = string[i:]
            if find_matching_brackets(subseq_brackets) == -1:
                return True
            else:
                subseq_brackets = string[i:find_matching_brackets(subseq_brackets) + i]
                if is_nested(subseq_brackets):

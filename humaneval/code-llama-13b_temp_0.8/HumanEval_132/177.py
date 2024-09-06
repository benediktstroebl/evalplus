
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
    # Brute Force
    #   O(n^2)
    #   O(1)
    #   n is the number of characters in the string
    def recursive_helper(string, counter):
        if len(string) == 0:
            if counter == 0:
                return True
            else:
                return False
        elif string[0] == '[':
            counter += 1
        elif string[0] == ']':
            counter -= 1
        return recursive_helper(string[1:], counter)
        
    return recursive_helper(string, 0)


    # def is_nested(string):
    #     count = 0
    #     for i in string:
    #         if i == '[':
    #             count += 1
    #         elif i == ']':
    #             if count == 0:
    #                 return False
    #             count -= 1
    #     if count == 0:
    #         return True
    #     return False


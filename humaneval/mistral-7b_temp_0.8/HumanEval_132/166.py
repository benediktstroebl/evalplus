
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
    # # Note: if any of the brackets are not paired properly, then the result will be False.
    # # So for this example, if the first square bracket is not paired with the last square bracket, then the result will be False.
    # # Similarly, if the second square bracket is not paired with the first square bracket, then the result will be False.
    # # So, in general, if any of the brackets are not paired properly, then the result will be False.

    # # So in order to make sure that the brackets are paired properly, we can use a nested for loop to check if each bracket is paired with its corresponding bracket.
    # for i in range(len(string)):
    #     for j in range(i + 1, len(string)):
    #         if string[i] == '[' and string[j] == ']':
    #             continue
    #         else:
    #             return False

    # return True




    if len(string) == 0:
        return False
    if

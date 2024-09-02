
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
    #   return True if at least one bracket in the subsequence is nested.
    #   use slicing to get the subsequence
    #   use a counter variable to count the number of brackets
    #   use an if statement to test whether or not the counter is even
    #   use a while loop to test the subsequence
    #   if there are an odd number of brackets the subsequence is nested
    #   return True
    #   else return False

    count_brackets = 0
    nested = False

    for i in range(len(string)):
        if string[i] == '[':
            count_brackets += 1
            subsequence = string[i+1:i+count_brackets+1]
            # print(subsequence)
            for x in subsequence:
                if x == ']':
                    count_brackets -= 1
            if count_brackets % 2 == 0:
                nested = False
            else:
                nested = True
            count_brackets = 0
    return nested


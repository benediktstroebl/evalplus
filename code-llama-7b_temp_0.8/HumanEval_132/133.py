
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

    #init vars
    left_brackets = 0
    right_brackets = 0
    matched_brackets = 0
    is_nested = False

    #loop thru each char in the string
    for char in string:

        #if this is a left bracket, count it
        if char == '[':
            left_brackets += 1

        #if this is a right bracket, count it
        elif char == ']':
            right_brackets += 1

            #check if we have enough right brackets
            if left_brackets > 0:

                #count the matched bracket pair
                matched_brackets += 1

                #if the matched brackets matches the left brackets, we know we have a nested bracket
                if left_brackets == matched_brackets:
                    is_nested = True

        else:
            raise TypeError("Only string that contains square brackets are allowed.")

    return is_nested

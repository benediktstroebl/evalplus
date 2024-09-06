
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
    # 🚨 Don't change the code below 👇
    string = list(string)
    result = []
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    opening = 0
    closing = 0
    for i in range(len(string)):
        if string[i] == '[':
            opening +=1
            result.append(opening - closing)
        elif string[i] == ']':
            closing +=1
            result.append(opening - closing)
    return max(result) > 0
    
    




    #Write your code above this row 👆
    
    # 🚨 Don't change the code below 👇
    print(result)
    print(max(result) > 0)
    return max(result) > 0


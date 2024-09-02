
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
    # Check if the string contains any brackets
    if '[' not in string:
        return False

    # Create an empty set to store all used brackets
    used_brackets = set()

    # Iterate over the string and replace all brackets with a unique integer
    for char in string:
        if char == '[':
            used_brackets.add(len(used_brackets))
        elif char == ']':
            used_brackets.remove(len(used_brackets))

    # Check if there is a nested bracket in the subsequence
    for i in range(len(used_brackets)):
        if used_brackets[i] > used_brackets[i + 1]:
            return True

    return False
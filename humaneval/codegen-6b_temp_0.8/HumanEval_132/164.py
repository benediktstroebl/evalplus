
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
    # What should the type be of characters in the input string?
    character_type = 'str'

    # What does this expression return if the input is not a type of character?
    false_value = False

    # This is a function that takes a string as input and checks whether there is a nested sequence of brackets in the string.
    # Can you use this function to create a function that takes a string and returns True or False
    # if there is a valid sequence of brackets present?
    def nested(string):
        # What does this expression return if string is not a type of character?
        false_value = False

        # What does this function do?
        def bracket_nested(string):
            odd_brackets = 0
            even_brackets = 0
            for i in range(len(string)):
                if string[i] == '[' and (i % 2) == 0:
                    odd_brackets += 1
                elif string[i] == '[' and (i % 2) == 1:
                    even_brackets += 1
                elif string[i] == ']' and (i % 2) == 0:
                    odd_brackets -= 1
                elif string[i] == ']' and (i % 2) == 1:
                    even_brackets -= 1

                if even_brackets < 0 or odd_brackets < 0:
                    return false_value

            if even_brackets == 0 and odd_brackets == 0:
                return true_value

        # What is the type of this expression?
        true_value = True

        # What is the purpose of this code?
        if type(string) != character_type:
            return false_value

        # What is the purpose of this code?
        if string.count('[') == string.count(']'):
            return true_value

        # What is the purpose of this code?
        if bracket_nested(string) is true_value:
            return true_value

    expected_type = 'bool'

    # Do you see any errors about the input type?
    if type(string) == expected_type:
        # Do you see any errors about the output type?
        if type(bracket_n

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

    # Turn the brackets into strings to be iterated over.
    string = list(string)

    # Add a zero to the end to make the loop end on the last element.
    string.append(0)

    # Keep track of whether or not we've found a nested element.
    # If so, we don't want to return True if we find a non-nested element.
    nested = False

    # We keep track of how many of each bracket we've seen
    open_counter, close_counter = 0, 0

    # Start the loop at the first element in the string.
    for i, bracket in enumerate(string):

        # If the bracket is a '['...
        if bracket == '[':

            # We've seen a nested bracket, so we can return True without looking for anything else.
            nested = True

            # We've also seen an opening bracket, so we increment the open counter.
            open_counter += 1

        # If the bracket is a ']'...
        elif bracket == ']':

            # If we've already seen a nested element, we don't want to return True if we find an unnested element.
            if nested:

                # We've also seen a closing bracket, so we increment the close counter.
                close_counter += 1

                # If the close counter is greater than the open counter, we know that a closing bracket isn't nested.
                # The loop will end, so we can return False.
                if close_counter > open_counter:
                    return False

            # If we've not seen a nested element yet, we can return True if we find a nested element.
            else:
                return True

        # If we reach the end of the loop, we know that if we've found a nested element we can return True.
        # But if we haven't found a nested element yet, we return False.
        if i == len(string) - 1 and nested == False:
            return False

    # If we haven't returned anything yet, we know that we've found a nested element, and it's the


def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Use a dictionary to map each character to its index in the ASCII table
    ascii_map = {ord(c): i for i, c in enumerate(string.ascii_uppercase)}
    # Use a stack to keep track of the current word and its characters
    stack = []
    # Use a queue to store the characters that need to be processed
    queue = []
    # Iterate through the string, character by character
    for c in s:
        # If the character is a letter, add it to the current word
        if c >= ord('a') and c <= ord('z'):
            if stack:
                # If a word is already in the stack, add the new character to it
                stack[-1] += c
            else:
                stack.append(c)
        # If the character is a digit, add it to the current word
        elif c >= ord('0') and c <= ord('9'):
            if stack:
                # If a word is already in the stack, add the new character to it
                stack[-1] += c
            else:
                stack.append(c)
        # If the character is not a letter or a digit, add it to the current word
        else:
            if stack:
                # If a word is already in the stack, add the new character to it
                stack[-1] += c
            else:
                stack.append(c)
                # Enqueue the current word with the characters in the correct order
                queue.append(stack.pop())
                # Push each character in the current word to the queue
                queue.append(c)
    # Return the final word and its corresponding characters in the correct order
    return ''.join(reversed(queue))
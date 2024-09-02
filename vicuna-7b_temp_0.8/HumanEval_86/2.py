
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
    # Use a stack to keep track of the current word and its ascii value
    # Use a dictionary to store the previous word and its ascii value
    # Use a dictionary to store the current word and its ascii value
    # Use a dictionary to store the previous word and its ascii value
    stack = []
    words = s.split()
    for word in words:
        if word in word_dict:
            ascii_value = word_dict[word]
        else:
            ascii_value = ord(word)
        if stack:
            current_word = stack[-1]
            if ord(current_word[-1]) > ascii_value:
                # If the last character of the current word is greater than the
                # ASCII value of the next character, add the current word to the
                # dictionary and start a new stack
                word_dict[current_word] = stack.pop()
                stack = [current_word]
            else:
                # If the last character of the current word is less than or equal to
                # the ASCII value of the next character, append the current word
                # to the previous word and start a new stack
                word_dict[current_word] += word
                stack = [word]
        else:
            # If the current word is the first word, start a new stack
            stack = [word]

    return " ".join(word_dict.values())

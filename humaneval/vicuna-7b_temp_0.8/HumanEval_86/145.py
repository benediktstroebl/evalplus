
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
    # Convert string to lowercase
    s = s.lower()
    # Initialize empty list to store characters of each word
    words = []
    # Iterate over the string
    for char in s:
        # If the character is a digit
        if char.isdigit():
            # Append it to the current word
            words[-1] += str(char)
        # If the character is a letter
        elif char.isalpha():
            # Split the string on the current word
            i = s.find(char)
            # Append the string before the split to the current word
            words.append(s[:i])
            # Add the character to an empty list
            words.append(list(char))
        # If the string is empty
        elif s.endswith(char):
            # Add the character to an empty list
            words.append(list(char))
    # Join the words with their corresponding characters in ascending order
    return ' '.join(''.join(sorted(w)) for w in words)
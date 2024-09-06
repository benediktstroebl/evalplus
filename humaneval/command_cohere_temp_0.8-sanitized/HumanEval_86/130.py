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
    # Use a list to store each word and letter according to its appearance in s
    l = s.split()
    # Sort the letters of each word seperately
    for i in range(0, len(l)):
        # Use an auxiliary variable to store the word with sorted letters
        temp = ''
        for j in range(0, len(l[i])):
            # Append the letter to temp and sort them
            temp += l[i][j]
            temp = temp.sort()
        # Replace the word in l with the word with sorted letters
        l[i] = temp
    # Convert the list back to a string to return it
    return ' '.join(l)
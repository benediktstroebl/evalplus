
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
    # Create a list with words in s
    words_list = s.split()

    # Create a list with only the first letters of each word
    first_letter_list = [word[0] for word in words_list]

    # Create a list with only the last letters of each word
    last_letter_list = [word[-1] for word in words_list]

    # Create a list with all the words except the first and last letter of each word
    middle_letters_list = []
    for word in words_list:
        word = word.strip(word[0] + word[-1])
        middle_letters_list.append(word)

    # Create a list with all the letters arranged in ascending order based on ascii value
    letters_list = []
    for word in middle_letters_list:
        for letter in word:
            letters_list.append(letter)
    letters_list.sort()

    # Combine the first and last letter list with the list of letters arranged in ascending order
    # based on ascii value
    final_list = first_letter_list + letters_list + last_letter_list

    # Convert the list to a string
    final_string = ' '.join(final_list)

    return final_string

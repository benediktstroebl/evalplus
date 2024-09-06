def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define the string ending criteria for the last character
    end_char_criteria = bool(txt) and (len(txt) > 0) and (isalpha(txt[-1]))
    # Check if the string ends with a space after the last character
    has_space_after_last_char = (txt[-1:] == " ")
    # Check if the last character is not part of a word
    is_last_char_in_word = any(txt.endswith(word) for word in txt.split())
    # Determine the overall result based on the criteria
    return end_char_criteria and not (has_space_after_last_char or is_last_char_in_word)
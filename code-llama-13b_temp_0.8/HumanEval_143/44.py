
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    # Make a list of the words in the sentence
    words = sentence.split()
    # Make a new sentence
    new_sentence = ''
    # For every word in the original sentence
    for word in words:
        # If the length of the word is prime
        if is_prime(len(word)):
            # Add the word to the new sentence
            new_sentence += word
            # If the word is not the last word in the sentence
            if word != words[-1]:
                # Add a space to the new sentence
                new_sentence += ' '
    # Return the new sentence
    return new_sentence


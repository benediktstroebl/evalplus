
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
    ### Validate input
    assert 1 <= len(sentence) <= 100, f"Invalid len(sentence): {len(sentence)}"
    assert sentence.isalpha(), f"Non-letter in {sentence}"

    words = sentence.split()
    # Create a list of words that are prime length
    word_list = []
    for word in words:
        if _is_prime(len(word)):
            word_list.append(word)

    # Re-assemble the words into a sentence
    return ' '.join(word_list)


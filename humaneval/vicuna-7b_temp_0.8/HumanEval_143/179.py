
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
    # Define a dictionary to store the lengths of the words
    word_lengths = {len(word) for word in sentence.split()}

    # Filter the dictionary to keep only the prime numbers
    prime_words = [len(word) for len_word in word_lengths if len_word > 1 and all(x > 2 for x in word_lengths.values())]

    # Sort the list of words by their lengths
    prime_words.sort()

    # Define a list to store the words
    result = []

    # Create the new string by appending the words to the result list
    for word in prime_words:
        result.append(word)

    # Create the new string by appending the result list
    new_sentence = ' '.join(result)

    return new_sentence

input_sentence = "You are given a string representing a sentence, the sentence contains some words separated by a space, and you have to return a string that contains the words from the original sentence, whose lengths are prime numbers, the order of the words in the new string should be the same as the original one."
output_sentence = words_in_sentence(input_sentence)

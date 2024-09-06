
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
    result = []
    low, high = 0, 0
    while high < len(sentence):
        if high + 1 < len(sentence) and is_prime(len(sentence[low:high + 1])):
            high += 1
        else:
            result.append(sentence[low:high])
            low = high
            high += 1

    return ' '.join(result)


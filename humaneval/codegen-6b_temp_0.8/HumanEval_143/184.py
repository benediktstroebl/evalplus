
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
    result = ''
    words = sentence.split(' ')
    for word in words:
        if is_prime_number(len(word)):
            result += word + ' '
    return result.strip()


assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
assert words_in_sentence("I like sanpshirts") == "like sanpshirt"
assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "the quick brown fox"

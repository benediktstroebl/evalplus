
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
    output = ''
    words = sentence.split(' ')
    for word in words:
        if is_prime(len(word)):
            output += word + ' '
    return output[:-1]


assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(5) is True
assert is_prime(7) is True
assert is_prime(23423) is True
assert is_prime(2639) is True
assert is_prime(3797) is True
assert is_prime(4567) is True


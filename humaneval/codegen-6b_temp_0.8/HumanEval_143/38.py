
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
    return " ".join(sorted(set(filter(is_prime, re.split('\\s+', sentence.strip())))))


assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
assert words_in_sentence("I am happy") == ""
assert words_in_sentence("Hello, My name is John") == "my name is"
assert words_in_sentence("Can I not make believe of a king, that he is not a king") == "king"
assert words_in_sentence("So he said, \"That is, I can not believe that he is not a king,\" but later he did it") == "he said"
assert words_in_sentence("I love you") == ""

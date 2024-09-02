
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
    # When a sentence is too long, it is easier to have a split
    # into smaller parts, rather than having a split algorithm.
    # This problem is a split into substrings,
    # and each substring is a word of length 1.
    # To split a sentence into substrings,
    # let us assume that a word has the form [a-z]{1,}
    # (i.e., a substring made of a single character).
    # We first get rid of all unnecessary spaces from the sentence,
    # then find all substrings,
    # and then count the number of substrings with length > 1.
    # It may be better to implement a Trie for this purpose.
    sentence = sentence.replace(" ", "")
    substrings = [sentence[i:j] for i in range(len(sentence)) for j in range(i + 1, len(sentence) + 1)]
    return " ".join(substrings).count(" ") * "".join(substrings).count("")

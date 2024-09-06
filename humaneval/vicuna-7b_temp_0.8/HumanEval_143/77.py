
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
    sentence = sentence.lower()
    words = sentence.split()
    n = len(words)
    words_list = [words[i:i+2] for i in range(0, n, 2)]
    result_string = ""
    for word in words_list:
        result_string += str(word)
    for i in range(1, n):
        if all(x.is_prime() for x in result_string):
            result_string = result_string[:i] + " " + result_string[i:]
            break
    return result_string
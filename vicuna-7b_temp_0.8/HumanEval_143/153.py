
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
    # first, we remove all special characters and numbers from the sentence
    sentence_without_special_chars = re.sub(r'[^\w\s]', '', sentence)

    # then, we generate all possible combinations of length 2 of the words in the sentence_without_special_chars
    combinations = [sentence_without_special_chars[i:j] for i in range(len(sentence_without_special_chars)) for j in range(len(sentence_without_special_chars)-i) if len(sentence_without_special_chars[i:j]) == 2]

    # we select the combination that contains only prime numbers
    combinations = [word for word in combinations if all(len(word) % 2 == 0 for len(word) in range(len(word))) if len(word) > 2]

    # we join the selected combinations and we return the result
    return ' '.join(combinations)

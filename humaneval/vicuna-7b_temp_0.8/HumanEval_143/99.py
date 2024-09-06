
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
    result = []
    for word in words:
        if len(word) > 1:
            if word[0] == word[-1]:
                prime_nums = [x for x in range(2, int(word[0] * len(word) ** 0.5) + 1) if x % 2 == 1]
                new_word = ""
                for num in prime_nums:
                    new_word += str(num)
                result.append(new_word)
                result.append(word)
    return " ".join(result)
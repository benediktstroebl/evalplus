
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
    words_list = sentence.split()
    count_dict = {}
    for word in words_list:
        count_dict[word] = count_dict.get(word, 0) + 1
    new_words = []
    for key, value in count_dict.items():
        if count_dict[key] % 2 == 0:
            new_words.append(key)
    words_in_sentence =''.join(new_words)
    return words_in_

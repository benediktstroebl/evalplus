
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
    words = sentence.split()
    prime_words = [word for word in words if word.is_prime()]
    if len(prime_words) == 0:
        return ""
    else:
        word_lengths = [len(word) for word in prime_words]
        if len(word_lengths) == 0:
            return ""
        else:
            sorted_word_lengths = sorted(word_lengths)
            if len(sorted_word_lengths) == 1:
                return "".join(prime_words)
            else:
                for i in range(1, len(sorted_word_lengths)):
                    for j in range(i, len(sorted_word_lengths)):
                        temp = "".join([prime_words[k] for k in range(i, len(prime_words))])
                        new_temp = "".join([temp[j - 1] + str(j), temp[i - 1] + str(i)])
                        if new_temp.is_prime():
                            return new_temp
                        else:
                            i += 1
                            j = j + 1
                            break
    return ""
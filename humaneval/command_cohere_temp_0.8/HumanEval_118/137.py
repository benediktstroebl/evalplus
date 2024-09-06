```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Using tuple to sort and count the frequency
    counter = dict()
    vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    word = word.lower()
    word = word[1:-1] if len(word) > 2 else word
    for letter in word:
        if letter in vowel:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
    # Search the max frequency value
    largest_freq = max(counter.values())
    # Search the vowel which max frequency
    for k, v in counter.items():
        if v == largest_freq:
            return k
    return ""
```
The following steps are used to solve it:
1. Store every vowel letters into a set.
2. Remove starting and ending vowels. We assume that starting and ending vowels don't count.
3. Use a counter to keep track the frequency of every letter.
4. Find the largest frequency.
5. Return the letter that max frequency. In case of a tie, return the earliest appearing letter. 

The solution relies on the fact that in English words, vowels tend to appear near consonants. This solution assumes that the vowels in the beginning and ending positions don't count as being "closest" to a consonant. It uses a counter to keep track of the frequency of each vowel and then finds the vowel(s) with the highest frequency, assuming that it is the closest vowel to a consonant in the word. 

The provided example tests cover different scenarios to validate the correctness of the function. You can further improve the solution by applying optimization in the code. For example, we can reduce our search space by ignoring punctuation and voweloids (letters that have similar sound to vowels, i.e. a y).
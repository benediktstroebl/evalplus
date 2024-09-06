
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Step 1: create a function that returns True if the string is a vowel, False otherwise.
    def vowel_checker(c):
        vowels = ["a", "e", "i", "o", "u"]
        return c in vowels
    
    # Step 2: iterate over the characters in the string
    result = []
    i = 0
    for i in range(len(s)):
        # Step 3: if the character is not a vowel, continue iterating over the string
        if not vowel_checker(s[i]):
            j = i
            # Step 4: count the number of non-vowels in a row
            counter = 0
            while not vowel_checker(s[j]):
                counter += 1
                j += 1
                # Step 5: if the number of non-vowels in a row is equal to the number n, append the word to the result
                if counter == n:
                    word = s[i:j]
                    result.append(word)
                # Step 6: if the number of non-vowels in a row is greater than n, break
                if counter > n:
                    break
                
    return result

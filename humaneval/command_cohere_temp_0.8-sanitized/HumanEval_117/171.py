def count_consonants(word):
    # Count consonants in the word
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
            not (char == 'y' and word[char_index:char_index + 2] != 'ay' and word[char_index:char_index + 2] != 'ey' and word[char_index:char_index + 2] != 'iy' and word[char_index:char_index + 2] != 'oy' and word[char_index:char_index + 2] != 'uy'):
            if char == 'c' or char == 'g':
                cnt += 1
            elif char == 'b' or char == 'd' or char == 'f' or char == 'h' or char == 'j' or char == 'k' or \
              char == 'l' or char == 'm' or char == 'n' or char == 'p' or char == 'q' or char == 'r' or \
              char == 's' or char == 't' or char == 'v' or char == 'w' or char == 'x' or char == 'y' or char == 'z':
                cnt += 2
        char_index += 1
    return cnt
def select_words(s, n):
    # Split string s into a list of words
    words = s.split()
    selected_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            selected_words.append(word)

    return selected_words
n = 3
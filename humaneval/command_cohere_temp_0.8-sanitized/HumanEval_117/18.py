def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                (char != 'y' or word[1:] != 'ay' and word[1:] != 'ey' and word[1:] != 'iy' and word[1:] != 'oy' and word[1:] != 'uy'):
            if char == 'b' or char == 'c' or char == 'd' or char == 'f' or char == 'g' or \
                    char == 'h' or char == 'j' or char == 'k' or char == 'l' or char == 'm' or \
                    char == 'n' or char == 'p' or char == 'q' or char == 'r' or char == 's' or \
                    char == 't' or char == 'v' or char == 'w' or char == 'x' or char == 'y':
                count += 1
    return count
def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
n = 3
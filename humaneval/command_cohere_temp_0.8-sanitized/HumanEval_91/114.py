def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == 'I':
            j = i + 1
            while j < len(words):
                if words[j] == '.' or words[j] == '?' or words[j] == '!':
                    break
                j += 1
                if j > i + 2 and (words[i + 1] == 'am' and words[i + 2] == 'boring') or \
                   (words[i + 1] == 'was' and words[i + 2] == 'boring') or \
                   (words[i + 1] == 'is' and words[i + 2] == 'boring'):
                    count += 1
                    break
                j += 1
    return count
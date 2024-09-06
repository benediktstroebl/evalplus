def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == 'I':
            j = i + 1
            while j < len(words):
                if words[j] == '.' or words[j] == '?' or words[j] == '!':
                    count += 1
                    break
                j += 1
    return count
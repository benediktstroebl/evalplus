def find_max(words):
    max_dict = max(zip(words, map(set, words)), key=lambda x: x[1].__len__())[0]
    return max_dict if max_dict == max(words, key=lambda x: x.lower()) else max(words, key=lambda x: x.lower())
def odd_count(strings):
    res = ['the number of odd elements in the string %s of the input.' % i for i in range(len(strings))]
    for i in range(len(strings)):
        odd = 0
        str1 = strings[i]
        for char in str1:
            if char % 2:
                odd += 1
        res[i] = str(odd)
    return res
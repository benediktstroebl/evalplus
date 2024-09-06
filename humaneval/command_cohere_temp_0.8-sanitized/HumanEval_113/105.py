def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
        .replace('1', 'the number of odd elements in the string ')
        .replace('0', 'the number of even elements in the string ')
        for s in lst]
    return r
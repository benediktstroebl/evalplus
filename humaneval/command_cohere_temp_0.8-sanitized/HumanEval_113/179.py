def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
        .replace('1', 'the number of odd elements in the string ')
        .replace('0', 'of the ')
        .replace('3', 'the number of odd elements ')
        .replace('2', 'of the ')
        .replace('5', 'the number of odd elements ')
        .replace('4', 'of the ')
        .replace('7', 'the number of odd elements ')
        .replace('6', 'of the ')
        .replace('9', 'the number of odd elements ')
        for s in lst]
    return r
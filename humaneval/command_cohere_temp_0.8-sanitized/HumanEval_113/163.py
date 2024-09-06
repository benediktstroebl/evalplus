def odd_count(lst):
    r = [str(len(re.findall(r'o*d*', s))) for s in lst]
    return ["the number of odd elements in the string %s of the input." % i for i in r]
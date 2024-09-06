def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
         .replace('1', 'n')
         .replace('3', 'n')
         .replace('5', 'n')
         .replace('7', 'n')
         .replace('9', 'n')
         for s in lst]
    return r
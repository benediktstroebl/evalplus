def match_parens(lst):
    def diff(s):
        return '(' if s == ')' else ')'
    
    both = [x for x in lst if x != '()]'][:2]
    count = [x for x in both if x == '(']
    if count.count(diff(count[0])) % 2 == 0:
        return "Yes"
    else:
        return "No"
def match_parens(lst):
    opens = {'(':0, '':1}
    closes = {')':0, '':1}
    sum_par = sum(opens.get(x,0) for x in lst[0]) - \
              sum(closes.get(x,0) for x in lst[1])
    return 'Yes' if sum_par == 0 else 'No'
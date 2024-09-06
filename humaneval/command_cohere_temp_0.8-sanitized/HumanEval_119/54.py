def match_parens(lst):
    def shift(s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            else:
                cnt -= 1
            yield from [char] * cnt

    combinations = [{char for char in shift(s)} for s in lst]
    
    def check_balance(combinations):
        return all(sum(cnt == 0 for cnt in balance) == 0 for balance in combinations)
    
    return "Yes" if check_balance(combinations) else "No"
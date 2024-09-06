def match_parens(lst):
    def bracket_count(s):
        return len(s) - len(s.replace('(', '').replace(')', ''))
    
    if bracket_count(lst[0]) == bracket_count(lst[1]):
        return "Yes"
    else: 
        return "No"
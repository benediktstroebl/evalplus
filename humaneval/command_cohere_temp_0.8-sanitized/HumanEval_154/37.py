def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    
    return second in first or any(second == sub for sub in first if sub == second[1:] or sub == second[:1])
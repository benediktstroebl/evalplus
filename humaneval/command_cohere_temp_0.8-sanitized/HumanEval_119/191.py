def match_parens(lst):
    def merge(a, b):
        count_a = count_b = 0
        current = a
        while count_a < len(a) or count_b < len(b):
            open_par = min(count_a, count_b)
            close_par = max(count_a, count_b)
            if current[-open_par:] == '(' * open_par:
                current += b[close_par - open_par:]
                count_a -= open_par
                count_b -= close_par
            elif current[-open_par:] == ')' * open_par:
                current += a[close_par - open_par:]
                count_a -= open_par
                count_b -= close_par
            else:
                return False
            if not count_a and not count_b:
                return True
        return False

    return "Yes" if any(merge(a, b) for a, b in zip(lst, lst[1:])) else "No"
def unique_digits(ls):
    even_digits = [ele for ele in ls if any(int(digit) % 2 == 0 for digit in str(ele))]
    return sorted(ele for ele in ls if not ele in even_digits)
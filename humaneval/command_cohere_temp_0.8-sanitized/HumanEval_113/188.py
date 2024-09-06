def odd_count(lst):
    r = []
    for idx, s in enumerate(lst):
        # count odd digits
        d = sum(1 for c in s if c % 2 == 1)
        # construct the output string
        r.append(f"the number of odd elements in the string {idx + 1} of the input."
                 .replace(f'{idx + 1}', f"{d}")
                 .replace('the number of odd elements in the string ', ''))
    return r
def odd_count(lst):
    r = []
    for num in lst:
        count = len(re.findall(r'o|O', num))
        r.append(f"the number of odd elements in the string {len(num)} of the input"
                  f". Odd digit(s): {count}")
    return r
def match_parens(lst):
    def check(s, arr):
        cnt = [0] * 2
        for ch in s:
            if ch == '(':
                cnt[0] += 1
            else:
                cnt[1] += 1
            if not arr[cnt[0]]:
                return False
            if not arr[cnt[1]]:
                return False
        return cnt[0] == cnt[1] == 0

    return "Yes" if any(map(check, lst)) else "No"
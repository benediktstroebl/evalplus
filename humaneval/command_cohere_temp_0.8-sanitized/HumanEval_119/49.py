def match_parens(lst):
    def check(s, arr):
        cnt = [0] * 2
        for ch in s:
            cnt[ch == '('] += 1
        for i in range(len(arr)):
            cnt[arr[i]] -= 1
        return all(cnt[i] >= 0 for i in range(2))
    
    arr = list(zip(*lst))
    arr.sort(key=lambda x: x[0])
    return 'Yes' if check(''.join(arr[0]), arr[1]) else 'No'
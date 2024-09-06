def match_parens(lst):
    def merge(a, b):
        depth_a = 0
        depth_b = 0
        curr = ''
        res = ''
        for c in a + b:
            if c == '(':
                if curr == ')':
                    res += ')'
                    depth_b -= 1
                else:
                    res += c
                    depth_a += 1
            elif c == ')':
                if curr == '(':
                    res += ')'
                    depth_a -= 1
                else:
                    res += c
                    depth_b += 1
            curr = c
        if max(depth_a, depth_b) == 0:
            return 'Yes'
        else:
            return 'No'

    if len(lst) != 2:
        return 'No'
    else:
        return merge(lst[0], lst[1])
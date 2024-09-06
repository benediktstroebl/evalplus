def match_parens(lst):
    def merge(a, b):
        depth_a, depth_b = 0, 0
        curr = 0
        for c in zip(a, b):
            if c == '(':
                if curr == 0:
                    depth_a += 1
                curr += 1
            elif c == ')':
                if curr == 0:
                    depth_b += 1
                curr -= 1
        return depth_b <= depth_a <= depth_b + max(curr, max(depth_a, depth_b))
    
    return "Yes" if any(merge(a, b) for a, b in zip(lst, lst[1:])) else "No"
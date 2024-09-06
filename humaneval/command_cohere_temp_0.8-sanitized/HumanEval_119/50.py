def match_parens(lst):
    def shift_tree(tree, shift):
        if not tree:
            return False
        if tree[0] == 'L':
            return shift_tree(tree[1:], shift+1) and shift_tree(tree[2:], shift)
        elif tree[0] == 'R':
            return shift_tree(tree[1:], shift-1) and shift_tree(tree[2:], shift)
        else:
            return shift_tree(tree[1:], shift) or (shift == 0 and tree[0] == '(')

    if len(lst) < 2:
        return 'No'
    elif len(lst) == 2:
        return 'Yes' if shift_tree(lst[0], 0) and shift_tree(lst[1], 0) else 'No'
    else:
        return 'Yes' if any(match_parens(sublist) == 'Yes' for sublist in lst) else 'No'
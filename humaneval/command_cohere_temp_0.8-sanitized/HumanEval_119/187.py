def match_parens(lst):
    def shift_brackets(brackets):
        result = []
        brackets = list(brackets)
        while brackets:
            if not brackets or brackets[0] == '(':
                result.append('(')
                brackets.remove('(')
            elif not brackets or brackets[0] == ')':
                result.append(')')
                brackets.remove(')')
            else:
                raise ValueError("Unexpected brackets sequence")
        return ''.join(result)

    return 'Yes' if len(lst) == 2 and shift_brackets(lst[0] + lst[1]) == '(()())' else 'No'
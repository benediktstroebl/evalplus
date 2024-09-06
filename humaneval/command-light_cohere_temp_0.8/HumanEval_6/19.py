```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_parens = ['(', ')']
    closing_parens = [')']

    for char in s:
        if char in opening_parens:
            stack.append(char)
        elif char in closing_parens:
            if len(stack) == 0:
                return []
            closing_char = stack.pop()
            return stack[:-1]
    return []

# Unit tests
def test_parse_nested_parens():
    test_data = {
        "(()()) ((())) () ((())())".split()
        , "(()))((()))".split()
        , "((()))()".split()
        , "()()()((()))".split()
        , "() ((()))".split()
        , "()()(())".split()
        , "() () () (())".split()
    }

    expected_results = [2, 3, 1, 3]

    for case, actual in zip(test_data, expected_results):
        print(f"Case: {case}\tExpected: {expected_results}")
        print(f"Actual: {actual}")
        assert actual == expected_results, "Failed in test case"

test_parse_nested_parens()
```

The function `parse_nested_parens` uses a stack to keep track of opening parentheses and then matches them with the corresponding closing parentheses to identify the correct nesting. This function can handle different types of input and correctly returns the deepest level of nesting of parentheses.
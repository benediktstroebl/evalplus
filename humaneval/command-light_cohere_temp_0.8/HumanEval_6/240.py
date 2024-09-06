```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    opening = True
    for c in parent_string:
        if opening and c == "(":
            stack.append(1)
            opening = False
        elif closing and c == ")":
            if stack:
                output.append(stack.pop()
            closing = False
            stack.append(0)
        else:
                opening = True
    return output


# Test case 1
test_case_1 = """(((())))""""


# Test case 2
test_case_2 = """(()())((()))(()))"""""


# Test case 3
test_case_3 = """()""""


# Test case 4
test_case_4 = """((()()))""""


# Test case 5
test_case_5 = """((()))""""


# Test case 6
test_case_6 = """())""""


# Test case 7
test_case_7 = """()""""


# Test case 8
test_case_8 = """()()()"


# Test case 9
test_case_9 = """()(())""


# Test case 10
test_case_10 = """()()(())()"


# Test case 11
test_case_11 = """((())()"


# Test case 12
test_case_12 = """())""


# Test case 13
test_case_13 = """(())""


def test():
    test_cases = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6, test_case_7, test_case_8, test_case_9, test_case_10, test_case_11, test_case_12, test_case_13]
    for t in test_cases:
        assert parse_nested_parens(t) == [2, 3, 1, 3]  # Tests for all inputs.
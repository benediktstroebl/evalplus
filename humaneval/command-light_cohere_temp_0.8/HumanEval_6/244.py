```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input.
    It returns a array of the deepest level of nesting.
    """
    string: str
    """

    def parse(self, string: str) -> List[int]:
        stack = []
        for match in string.group() :
            if match == '(' :
                stack.append(1)
                else :
                    stack.append(len)
            stack.extend(1)
        stack.pop()
        = 0
            for match in string.stack[::-1]
            return stack
    """

    @test_parse_nested_parens
    assert parse('(()()) ((())) () ((())()())')', [2, 3, 1, 3])
    assert parse('(()()) () ((()))()', [2, 3, 1])
    assert parse('(()())()()()()()()()()', [2, 3, 1])
    assert parse('()()(()())()()()()()()()()', [2, 3, 1])
    assert parse('(()())()()()()()()()()()()', [2, 3, 1, 2])
    assert parse('(()())()()()(()())()()()()', [2, 3, 2])
    assert parse('(()())()(()())()()()()()', [2, 3, 1, 3])
    assert parse('()()()()(()())()()()()()()', [2, 3, 1])
    assert parse('()()(()())()()()()()()()()()', [2, 3, 1, 2])

    @test_parse_nested_parens
    def test():
        assert parse('(()())()()()()()()()', [2, 3, 1])
    test()  # pass the test function
    ```
```python
def parse_nested_parens(s: str) -> List[int]:
    """
    This function will take a string with nested parentheses as input and will return the deepest level of nesting of the parentheses.
    Parameters:
        s (string): The string with nested parentheses
    Returns:
        List[int]: The deepest level of nesting of the parentheses.
    """
    def test_parse_nested_parens() -> None:
        """
        This function tests the parse_nested_parens function with various inputs.
        """
        For the test will two different inputs, and asserts the outputs are as expected.
        """
        assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3],
        assert parse_nested_parens('()()()()()()()()()()()') == [4, 2, 1, 3]
        assert parse_nested_parens('() () (()) () (())()()') == [4, 2, 1, 3]
        assert parse_nested_parens('(())()()()()()()()()()()') == [4, 3, 1, 2]
        assert parse_nested_parens('((()))()()()()()()()()()()()') == [5, 1]
        assert parse_nested_parens('()()()()()()()()()())' == [4, 3, 1]
        assert parse_nested_parens('() (()) ()()()()()') == [4, 2, 1]
        assert parse_nested_parens('() () () (()) ()()()') == [4, 2, 1]
        assert parse_nested_parens('() () (()) ()() ()()') == [4, 2, 1]
        assert parse_nested_parens('() () () () () ()()') == [4, 2, 1]
        assert parse_nested_parens('() () () (()) ()()') == [4, 2, 1]
        assert parse_nested_parens('() (()) () () ()()') == [4, 3, 1]
        assert parse_nested_parens('() () () () () ()') == [4, 3, 1]
        assert parse_nested_parens('() () () () () () ()') == [4, 3, 1]
        assert parse_nested_parens('() () ()) () () () () () ()') == [5, 1]
        assert parse_nested_parens('( )() () () () () () ()') == [5, 1]
        assert parse_nested_parens('() () ()) () () () () () ()') == [5, 1]
        assert parse_nested_parens('( )() () ()) () () () () ()') == [5, 1]
        assert parse_nested_parens('( )() () ()) ( ) () () () ()') == [5, 1]
        assert parse_nested_parens('() ( ) ( ) ( ) ( ) ( ) ( )') == [5, 1]
        assert parse_nested_parens('() ( ) ( ) () ( ) () ()') == [5, 1]
        assert parse_nested_parens('() ( ) ( ) ( ) ( ) () ( )') == [5, 1]
        assert parse_nested_parens('() ( ) ( ) () ( ) () ( )') == [5, 1]
        assert parse_nested_parens('() ( ) ( ) ()
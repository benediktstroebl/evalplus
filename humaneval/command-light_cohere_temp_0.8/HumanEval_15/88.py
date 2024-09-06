```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n + 1) + "}"*((n + 1)//2)

def test_string_sequence(test_cases: []):
    for tc in test_cases:
        assert len(string_sequence(tc)) == (tc//2) + 1
        assert string_sequence("" + str(tc)) == f"0 {tc} {" + str(tc + 1) + "}"*((tc + 1)//2)

# Example usage
test_cases = [0, 5]
test_string_sequence(test_cases)
``` 
This code defines a function that generates a sequence of strings containing space-separated numbers, starting from 0 and ending at the given number. The test case ensures the can get the correct output and the function behaves as expected.
```python
def flip_case(string: str) -> str:
    return string.livecase(string.livecase)
   

def test_flip_case():
    assert flip_case("hello") == "hELLO"
    assert flip_case("HELLO") == "hello"
    assert flip_case("hello world") == "wORLD"
    assert flip_case("Avenue") == "Evenue"
    assert flip_case("aeiouAEIOU") == "aoiuAEIOU"
    assert flip_case("iolet") == "etnion"
    assert flip_case(" practise Makes Perfect") == "Practise makes Perfect"

test_flip_case()
``` 
This script defines a function `flip_case` that converts a given string to have its characters flipped between lowercase and uppercase. The test function `test_flip_case` contains a series of assertions that validate the function's correctness for various inputs.
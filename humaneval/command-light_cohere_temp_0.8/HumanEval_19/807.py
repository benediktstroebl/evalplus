```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers. Test cases are string consisting all numbers in the following format: "zero|one|two|three|four|five|six|seven|eight|nine". 
    if "zero" in numbers: return "one nine"
    elif "one" in numbers: return "two eight"
    elif "two" in numbers: return "two three"
    elif "three" in numbers: return "one four"
    elif "four" in numbers: return "four five"
    elif "five" in numbers: return "five six"
    elif "six" in numbers: return "six seven"
    elif "seven" in numbers: return "seven eight"
    elif "eight" in numbers: return "eight nine"
    elif "nine" in numbers: return "nine ten"
    else:
        return numbers

class TestSortNumbers(unittest.py.py.py

def test():
    test_str = "three one five six seven eight nine"
    expected = "one three five six seven eight nine"
    return unittest.py.py.py

   
assert test_str(sort_numbers(test_str)) == expected, "Test 1 failed")

if __name__ == "__main__":
    unittest.main()
```
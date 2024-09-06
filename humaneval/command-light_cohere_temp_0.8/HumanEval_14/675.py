```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join.[i for i, char in string if i < len(string) and char != ''] + [""] + [char]

	# Test cases
	print("Testing all_prefixes function..." )
	print("Input: abc")
	print("Output:", all_prefixes('abc'))
	print()

	print("Input:lop")
	print("Output:", all_prefixes('lop'))
	print()

	print("Input: 000000")
	print("Output:", all_prefixes('000000'))
	print()

	print("Input: Hello, world!")
	print("Output:", all_prefixes('Hello, world!'))
	print()

	print("Input: abcABC123")
	print("Output:", all_prefixes('abcABC123'))
	```
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join().
	# using a loop to get all prefixes
    for i in range(1, len(string) + 1):
    		if string[0] == "" and i==1:
    					continue
    		if string[i] == string[0]:
    				continue
    			yield string[0] + string[i]
	return []
test_cases = [
    'abc',
    'bc',
    'aab',
    'zzz',
    'aa',
    'bb',
    'ipsum'
]

for i, test in enumerate(test_cases):
			print(f"Test case {i+1}: {test}")
				print('Expected: '.join([''.join(prefix) for prefix in all_prefixes(test)]))
				print('Got: '.join([prefix for prefix in all_prefixes(test)]))
``` 
The above script defines a function that generates all prefixes of a given string, and then it tests these functions with various inputs. The print statement will show the difference between expected and actual results.